from RiotAPI import RiotAPI
from idToName import idToNameDict
from collections import Counter, namedtuple
import time


class GetData(object):
    
    def __init__(self, region):
        self.api = RiotAPI(region)
    
    def get_summoner_data(self, current_summoner):
       
        # Get summoner data, or tell us it couldn't be found
        try:
            summoner_response = self.api.get_summoner_by_name(current_summoner)
        except:
            exit('Summoner name {} does not exist'.format(current_summoner))
    
        # Parse the output and make sure we have both a person's summoner name and id
        summoner_id = (summoner_response[current_summoner]['id'])
        summoner_name = str(summoner_response[current_summoner]['name'])

        return summoner_id, summoner_name

    def get_summoners_mastery(self, summoner_id, summoner_name, num_champs):
        # Get a summoner's top <num_champs> champion mastery data
        try:
            mastery_response = self.api.get_top_mastery_data(summoner_id, num_champs)
        except:
            exit('Could not get champion mastery data for {}'.format(summoner_name))

        # Compile the stuff we care about into a dictionary (namely that champion id and its associated score)
        try:
            champ_points_pair = {item['championId']: item['championPoints'] for item in mastery_response}
        except:
            exit('We encountered a problem parsing champion mastery data for {}'.format(summoner_name))

        return champ_points_pair

    def lanes_and_roles(self, summoner_id, summoner_name, champ_points_pair):
        # Get data about regarding the lane the champion is being played in by checking the summoner's ranked history
        champ_list = [key for key in champ_points_pair]
        try:
            lane_response = self.api.get_champion_role(summoner_id, champ_list)
            while lane_response == {'status': {'status_code': 429, 'message': '429'}}:
                #print('429 code')
                time.sleep(5)
                lane_response = self.api.get_champion_role(summoner_id, champ_list)

        except:
            exit('Error trying to determine what lane one of the champions was played in by {}'.format(summoner_name))

        list_of_games = lane_response['matches']
        champ_role_time_in_role = {}
        for game in list_of_games:
            game_champion_id = game['champion']
            if 'lane' in game:
                lane_played = game['lane'].upper()
                if lane_played == 'BOTTOM':
                    role_played = game['role']
                else:
                    role_played = lane_played
                if ((lane_played == 'MID' and role_played =='DUO_SUPPORT') or
                    (lane_played == 'TOP' and role_played =='DUO_SUPPORT') or
                    (role_played == 'NONE')):
                    role_played = 'NONE'
                    continue
                if game_champion_id not in champ_role_time_in_role:
                    champ_role_time_in_role[game_champion_id] = Counter()
                champ_role_time_in_role[game_champion_id][role_played] += 1

        return champ_role_time_in_role

    def percentages(self, champ_counters):
        # Get percentage of games played in each role per champion (eg 33% top, 50% jungle, 17% support)
        # Bonus points if you can tell us what champions might fit that above percentage distribution

        for id_key, count_dict in champ_counters.items():
            role_games = 0
            for role_name, role_count in count_dict.items():
                role_games += role_count
            for role_name, role_count in count_dict.items():
                if role_games > 0:
                    champ_counters[id_key][role_name] /= float(role_games)
                else:
                    champ_counters[id_key][role_name] /= float(1)

        return champ_counters

    def data_compile(self, summoner_name, champ_counters, champ_points_pair):
        # Compile all the data that we have pulled so far into one place
        structured_data = []

        # Get the champion name for later use, because 'champion 35' doesn't mean much to people
        champion_name_dict = {champ_id: idToNameDict[champ_id] for champ_id in champ_counters}
        Champ = namedtuple('Champ', ['name', 'id', 'role', 'points', 'player'])

        try:
            # Create a list of things a person plays. A "thing" is a champion, role, points tuple
            # So one champion played in two roles will count as two things
            for id, name in champion_name_dict.items():
                if len(champ_counters[id]) == 1:
                    multiplier = 1
                elif len(champ_counters[id]) > 1:
                    multiplier = 1.25
                else:
                    exit('The champion has no listed roles')
                for role, percentage in champ_counters[id].items():
                    if role.upper() not in ['DUO_CARRY', 'DUO_SUPPORT', 'JUNGLE', 'MID', 'TOP']:
                        continue
                    points = int(percentage * multiplier * champ_points_pair[id])
                    champ_tuple = Champ(name, id, role, points, summoner_name)
                    structured_data.append(champ_tuple)

        except:
            exit('Error structuring the champion data for current summoner')

        return structured_data
