import api_calls
from backup_lane_guesses import backups
from collections import Counter, namedtuple


def get_summoner_data(current_summoner, region):

    try:
        # Get summoner data, or tell us it couldn't be found
        summoner_response = api_calls.summoner_lookup(current_summoner, region)
        # Parse the output and make sure we have both a person's summoner name and id
        summoner_id = summoner_response['id']
        summoner_name = summoner_response['name']
        account_id = summoner_response['accountId']
    except:
        raise KeyError('Summoner "{0}" does not exist in the {1} region'.format(current_summoner, region))

    return summoner_id, summoner_name, account_id


def get_summoners_mastery(summoner_id, summoner_name, num_champs, region):
    # Get a summoner's top <num_champs> champion mastery data
    try:
        mastery_response = api_calls.champion_mastery(summoner_id, num_champs, region)
    except:
        raise KeyError('Could not get champion mastery data for {}'.format(summoner_name))

    # Compile the stuff we care about into a dictionary (namely that champion id and its associated score)
    # Bonus multiplier for level 7/level 6 champions
    try:
        multiplier = {7: 1.5,
                      6: 1.2,
                      5: 1,
                      4: 1,
                      3: 1,
                      2: 1,
                      1: 1}
        champ_points_pair = {item['championId']: int(item['championPoints'] * multiplier[item['championLevel']])
                             for item in mastery_response}
    except:
        raise KeyError('We encountered a problem parsing champion mastery data for {}'.format(summoner_name))

    return champ_points_pair


def lanes_and_roles(account_id, summoner_name, champ_points_pair, champ_id_to_name, region):
    # Get data about regarding the lane the champion is being played in by checking the summoner's ranked history
    champ_list = [key for key in champ_points_pair]
    champ_role_time_in_role = {}
    try:
        lane_response = api_calls.match_history(account_id, champ_list, region)

    except:
        raise KeyError('Error trying to determine what lane one of the champions was played in by {}'.format
                       (summoner_name))

    try:
        list_of_games = lane_response['matches']
        for game in list_of_games:
            # Skip TT games
            if game['queue'] == 41:
                continue
            champ_id = game['champion']
            if 'lane' in game:
                lane_played = game['lane'].upper()

                if lane_played == 'BOTTOM':
                    role_played = game['role']

                else:
                    role_played = lane_played
                # If the API returns something that doesn't make any sense, make a guess as to where that champ
                # was played based off of hard coded values in BackupLaneGuess
                if ((lane_played == 'MID' and role_played =='DUO_SUPPORT') or
                        (lane_played == 'TOP' and role_played =='DUO_SUPPORT') or
                        role_played == 'NONE' or
                        role_played == 'SOLO' or
                        role_played == 'DUO'):
                    if str(champ_id) in backups:
                        champ_name = champ_id_to_name[str(champ_id)]
                        role_played = backups[champ_name]
                    else:
                        continue
                if champ_id not in champ_role_time_in_role:
                    champ_role_time_in_role[champ_id] = Counter()
                champ_role_time_in_role[champ_id][role_played] += 1

    except:
        pass

    # If the person hasn't played ranked, make a guess as to where they should play that champion based off
    # of hard coded values in BackupLaneGuess
    for champ_id in champ_list:
        if champ_id not in champ_role_time_in_role.keys():
            champ_name = champ_id_to_name[str(champ_id)]
            champ_role_time_in_role[champ_id] = Counter()
            champ_role_time_in_role[champ_id][backups[champ_name]] += 1

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
        raise KeyError('Error structuring the champion data for {}'.format(summoner_name))

    return structured_data
