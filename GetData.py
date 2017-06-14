import API
from collections import Counter, namedtuple

    
def get_summoner_data(current_summoner, region):

    # Get summoner data, or tell us it couldn't be found
    try:
        summoner_response = API.summoner_lookup(current_summoner, region)
    except:
        exit('Summoner name {} does not exist'.format(current_summoner))

    # Parse the output and make sure we have both a person's summoner name and id
    summoner_id = summoner_response['id']
    summoner_name = summoner_response['name']
    account_id = summoner_response['accountId']

    return summoner_id, summoner_name, account_id


def get_summoners_mastery(summoner_id, summoner_name, num_champs, region):
    # Get a summoner's top <num_champs> champion mastery data
    try:
        mastery_response = API.champion_mastery(summoner_id, num_champs, region)
    except:
        exit('Could not get champion mastery data for {}'.format(summoner_name, num_champs))

    # Compile the stuff we care about into a dictionary (namely that champion id and its associated score)
    # Bonus multiplier for level 7/level 6 champions
    try:
        multiplier = {7: 1.5, 6: 1.2, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}
        champ_points_pair = {item['championId']: int(item['championPoints'] * multiplier[item['championLevel']])
                             for item in mastery_response}
    except:
        exit('We encountered a problem parsing champion mastery data for {}'.format(summoner_name))

    return champ_points_pair


def lanes_and_roles(account_id, summoner_name, champ_points_pair, region):
    # Get data about regarding the lane the champion is being played in by checking the summoner's ranked history
    champ_list = [key for key in champ_points_pair]
    try:
        lane_response = API.match_history(account_id, champ_list, region)

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
                continue
            if game_champion_id not in champ_role_time_in_role:
                champ_role_time_in_role[game_champion_id] = Counter()
            champ_role_time_in_role[game_champion_id][role_played] += 1

    return champ_role_time_in_role


def percentages(champ_counters):
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


def data_compile(summoner_name, champ_counters, champ_id_to_name, champ_points_pair):
    # Compile all the data that we have pulled so far into one place
    structured_data = []

    # Get the champion name for later use, because 'champion 35' doesn't mean much to people
    champ_id_to_name = {key: value['name'] for key, value in champ_id_to_name.items()}
    Champ = namedtuple('Champ', ['name', 'id', 'role', 'points', 'player'])

    try:
        # Create a list of things a person plays. A "thing" is a champion, role, points tuple
        # So one champion played in two roles will count as two things
        for champ_id, champ_info in champ_counters.items():
            if len(champ_counters[champ_id]) == 1:
                multiplier = 1
            elif len(champ_counters[champ_id]) > 1:
                multiplier = 1.25
            else:
                exit('The champion has no listed roles')
            for role, percentage in champ_info.items():
                if role.upper() not in ['DUO_CARRY', 'DUO_SUPPORT', 'JUNGLE', 'MID', 'TOP']:
                    continue
                name = champ_id_to_name[str(champ_id)]
                points = int(percentage * multiplier * champ_points_pair[champ_id])
                champ_tuple = Champ(name, champ_id, role, points, summoner_name)
                structured_data.append(champ_tuple)

    except:
        exit('Error structuring the champion data for current summoner')

    return structured_data
