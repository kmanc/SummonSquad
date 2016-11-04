from RiotAPI import RiotAPI
import json
import operator
import KeyAPI as Key
import sys


class GetData(object):
    
    def _gimme_data(self, current_summoner, champs, region):
        
        api = RiotAPI(Key.KEY['key'], region)
        champ_points_pair = {}
        champList = []
        champ_role_timeinrole = {}
        structured_data = {}
        champion_name = {}
       
        # Get summoner data, or tell us it couldn't be found
        try:
            summoner_response = api.get_summoner_by_name(current_summoner)
        except:
            sys.exit('Summoner name ' + current_summoner + ' does not exist')
    
        # Parse the output and make sure we have both a person's summoner name and id
        temp = json.dumps(summoner_response)
        temp = json.loads(temp)
        summoner_id = (temp[current_summoner]['id'])
        summoner_name = (temp[current_summoner]['name'])
    
        # NOT USED FOR THIS PROJECT AT THIS TIME
        # Get all of a summoner's mastery data
        #response = api.get_summoner_mastery_data(summoner_id)
        #print (response)
    
        # Get a summoner's top X champion mastery data
        try:
            mastery_response = api.get_top_mastery_data(summoner_id, champs)
        except:
            sys.exit('Could not get champion mastery data for ' + current_summoner)
    
        # Compile the stuff we care about into a dictionary (namely that champion id and its associated score)
        for x, val in enumerate(mastery_response):
            try:
                champ_points_pair[val['championId']] = val['championPoints']
            except:
                sys.exit('We encountered a problem parsing champion mastery data for ' + current_summoner)
    
        # Get data about regarding the lane the champion is being played in by checking the summoner's arnked history
        for key in champ_points_pair:
            champList.append(key)
        try:
            lane_response = api.get_champion_role(summoner_id, champList)
            #print(lane_response)
        except:
            sys.exit('Error trying to determine what lane one of the champions was played in by ' + current_summoner)
    
        # Figure out what roles the champion is being played in, and for how many games (eg. mid 10 times, support 4 times)
        match_check = 'matches'
        if match_check in lane_response:
            for x, val in enumerate(lane_response['matches']):
                key_test = val['champion']
                if ('lane' in val):
                    if (val['lane'] == 'BOTTOM'):
                        role = val['role']
                    else:
                        role = val['lane']
                    if (val['lane'] == 'MID' and val['role'] == 'DUO_SUPPORT'):
                        role = 'NONE'
                    if (val['lane'] == 'TOP' and val['role'] == 'DUO_SUPPORT'):
                        role = 'NONE'
                    if key_test not in champ_role_timeinrole:
                        champ_role_timeinrole[key_test] = {}
                    else:
                        if role in champ_role_timeinrole[key_test]:
                            champ_role_timeinrole[key_test][role] += 1
                        else:
                            champ_role_timeinrole[key_test][role] = 1
    
        # Get percentage of games played in each role per champion (eg 33% top, 50% jungle, 17% support)
        # Bonus points if you can tell us what champions might fit that above percentage distribution
        
        #########################################
        #### UNCOMMENT THE BELOW FOR SOME INSIGHT INTO THE CRASHES.  SOMETIMES A SUMMONER WILL HAVE NO CHAMPION/MASTERY PAIRS
        #########################################
        #print(champ_role_timeinrole)
        if not champ_role_timeinrole:
            print()
            print('SOMEBODYs FUCKING CHAMP DICTIONARY IS FUCKING EMPTY...WHY')
            print(current_summoner)
            print()
        for id_key in champ_role_timeinrole:
            role_games = 0
            for role_key in champ_role_timeinrole[id_key]:
                role_games += champ_role_timeinrole[id_key][role_key]
            for role_key in champ_role_timeinrole[id_key]:
                if role_games > 0:
                    champ_role_timeinrole[id_key][role_key] /= role_games
                else:
                    champ_role_timeinrole[id_key][role_key] /= 1
                    
        # Get the champion name for later use, because 'champion 34' doesn't mean much to people
        for champIdizzle in champ_points_pair:
            try:
                champion_response = api.get_champion_name(champIdizzle)
                champion_name[champIdizzle] = (champion_response['name'])
            except:
                sys.exit('Could not get the name of the champ with id ' + champIdizzle)
        
        # Compile all the data that we have pulled so far into one place
        try:
            # Put summoner id as a first level key
            structured_data[summoner_id] = {}
    
            # Put champion id as a second level key, with the name and another dictionary as the value
            for champion_id in champion_name:
                structured_data[summoner_id][champion_id] = [champion_name[champion_id]]
        
            # Put role as a third level key with mastery points * percentage of games in that role as the value
            for second_champ_id in champ_role_timeinrole:
                for role in champ_role_timeinrole[second_champ_id]:
                    structured_data[summoner_id][second_champ_id].append(
                                                    {role: champ_role_timeinrole[second_champ_id][role] * 
                                                    champ_points_pair[second_champ_id]})
                                                
            # Check to make sure each champion has at least a value for points; if it doesn't, make it 0
            for x, champion_id in enumerate(structured_data[summoner_id]):
                if (len(structured_data[summoner_id][champion_id]) == 1):
                    structured_data[summoner_id][champion_id].append({'NONE': 0.0})

        except:
            sys.exit('Error structuing the champion data for ' + current_summoner)

        return structured_data
