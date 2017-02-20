from RiotAPI import RiotAPI
from idToName import idToNameDict
import time

class GetData(object):
    
    def _setup(self, region):
        self.api = RiotAPI(region)
    
    def _gimme_data(self, current_summoner, champs):
        
        champ_points_pair = {}
        champList = []
        champ_role_timeinrole = {}
        structured_data = {}
        champion_name = {}
       
        # Get summoner data, or tell us it couldn't be found
        try:
            summoner_response = self.api.get_summoner_by_name(current_summoner)
        except:
            exit('Summoner name {} does not exist'.format(current_summoner))
    
        # Parse the output and make sure we have both a person's summoner name and id
        summoner_id = (summoner_response[current_summoner]['id'])
        summoner_name = (summoner_response[current_summoner]['name'])
    
        # Get a summoner's top X champion mastery data
        try:
            mastery_response = self.api.get_top_mastery_data(summoner_id, champs)
        except:
            exit('Could not get champion mastery data for {}'.format(current_summoner))
    
        # Compile the stuff we care about into a dictionary (namely that champion id and its associated score)
        for x, val in enumerate(mastery_response):
            try:
                champ_points_pair[val['championId']] = val['championPoints']
            except:
                exit('We encountered a problem parsing champion mastery data for {}'.format(current_summoner))
    
        # Get data about regarding the lane the champion is being played in by checking the summoner's arnked history
        for key in champ_points_pair:
            champList.append(key)
        try:
            lane_response = self.api.get_champion_role(summoner_id, champList)
            while lane_response == {'status': {'status_code': 429, 'message': '429'}}:
                #print('429 code')
                time.sleep(5)
                lane_response = self.api.get_champion_role(summoner_id, champList)

        except:
            exit('Error trying to determine what lane one of the champions was played in by {}'.format(current_summoner))
    
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
        """if not champ_role_timeinrole:
            print('SOMEBODYs FUCKING CHAMP DICTIONARY IS FUCKING EMPTY...WHY')
            print()
            print(current_summoner)
            print()"""
        for id_key in champ_role_timeinrole:
            role_games = 0
            for role_key in champ_role_timeinrole[id_key]:
                role_games += champ_role_timeinrole[id_key][role_key]
            for role_key in champ_role_timeinrole[id_key]:
                if role_games > 0:
                    champ_role_timeinrole[id_key][role_key] /= float(role_games)
                else:
                    champ_role_timeinrole[id_key][role_key] /= float(1)
                    
        # Get the champion name for later use, because 'champion 34' doesn't mean much to people
        for champIdConvert in champ_points_pair:
            try:
                champion_name[champIdConvert] = idToNameDict[champIdConvert]
            except:
                exit('Could not get the name of the champ with id {}'.format(champIdConvert))
        
        # Compile all the data that we have pulled so far into one place
        try:
            # Put summoner id as a first level key
            structured_data[summoner_id] = {}
            # Put champion id as a second level key and the champion name as third level
            # Then put role as the fourth level and the points as the final value
            for champion_id in champ_role_timeinrole.keys():
                structured_data[summoner_id][champion_id] = {}
                structured_data[summoner_id][champion_id][champion_name[champion_id]] = {}
                for role in champ_role_timeinrole[champion_id]:
                    structured_data[summoner_id][champion_id][champion_name[champion_id]][str(role)] = \
                    champ_role_timeinrole[champion_id][role] * champ_points_pair[champion_id]
                if (len(structured_data[summoner_id][champion_id][champion_name[champion_id]].keys())) == 0:
                    structured_data[summoner_id][champion_id][champion_name[champion_id]] = {'None': 0}

        except:
            exit('Error structuing the champion data for {}'.format(current_summoner))

        return structured_data
