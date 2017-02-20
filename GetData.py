from RiotAPI import RiotAPI
import KeyAPI as Key
import time

idToNameDict = {
    266: 'Aatrox',
    103: 'Ahri',
    84: 'Akali',
    12: 'Alistar',
    32: 'Amumu',
    34: 'Anivia',
    1: 'Annie',
    22: 'Ashe',
    136: 'AurelionSol',
    268: 'Azir',
    432: 'Bard',
    53: 'Blitzcrank',
    63: 'Brand',
    201: 'Braum',
    51: 'Caitlyn',
    164: 'Camille',
    69: 'Cassiopeia',
    31: 'Cho\'Gath',
    42: 'Corki',
    131: 'Diana',
    122: 'Darius',
    119: 'Draven',
    36: 'Dr.Mundo',
    245: 'Ekko',
    60: 'Elise',
    28: 'Evelynn',
    81: 'Ezreal',
    9: 'Fiddlesticks',
    114: 'Fiora',
    105: 'Fizz',
    3: 'Galio',
    41: 'Gangplank',
    86: 'Garen',
    150: 'Gnar',
    79: 'Gragas',
    104: 'Graves',
    120: 'Hecarim',
    74: 'Heimerdinger',
    420: 'Illaoi',
    39: 'Irelia',
    427: 'Ivern',
    40: 'Janna',
    59: 'JarvanIV',
    24: 'Jax',
    126: 'Jayce',
    202: 'Jhin',
    222: 'Jinx',
    429: 'Kalisata',
    43: 'Karma',
    30: 'Karthus',
    38: 'Kassadin',
    55: 'Katarina',
    10: 'Kayle',
    85: 'Kennen',
    121: 'Kha\'Zix',
    203: 'Kindred',
    240: 'Kled',
    96: 'Kog\'Maw',
    7: 'LeBlanc',
    64: 'Lee Sin',
    89: 'Leona',
    127: 'Lissandra',
    236: 'Lucian',
    117: 'Lulu',
    99: 'Lux',
    54: 'Malphite',
    90: 'Malzahar',
    57: 'Maokai',
    11: 'MasterYi',
    21: 'MissFortune',
    82: 'Mordekaiser',
    25: 'Morgana',
    267: 'Nami',
    75: 'Nasus',
    111: 'Nautilus',
    76: 'Nidalee',
    56: 'Nocturne',
    20: 'Nunu',
    2: 'Olaf',
    61: 'Orianna',
    80: 'Pantheon',
    78: 'Poppy',
    133: 'Quinn',
    33: 'Rammus',
    421: 'Rek\'Sai',
    58: 'Renekton',
    107: 'Rengar',
    92: 'Riven',
    68: 'Rumble',
    13: 'Ryze',
    113: 'Sejuani',
    35: 'Shaco',
    98: 'Shen',
    102: 'Shyvana',
    27: 'Singed',
    14: 'Sion',
    15: 'Sivir',
    72: 'Skarner',
    37: 'Sona',
    16: 'Soraka',
    50: 'Swain',
    134: 'Syndra',
    223: 'TahmKench',
    91: 'Talon',
    163: 'Taliyah',
    44: 'Taric',
    17: 'Teemo',
    412: 'Thresh',
    18: 'Tristana',
    48: 'Trundle',
    23: 'Tryndamere',
    4: 'TwistedFate',
    29: 'Twitch',
    77: 'Udyr',
    6: 'Urgot',
    110: 'Varus',
    67: 'Vayne',
    45: 'Veigar',
    161: 'Vel\'Koz',
    254: 'Vi',
    112: 'Viktor',
    8: 'Vladimir',
    106: 'Volibear',
    19: 'Warwick',
    62: 'Wukong',
    101: 'Xerath',
    5: 'XinZhao',
    157: 'Yasuo',
    83: 'Yorick',
    154: 'Zac',
    238: 'Zed',
    115: 'Ziggs',
    26: 'Zilean',
    143: 'Zyra'
}

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
            exit('Summoner name {} does not exist'.format(current_summoner))
    
        # Parse the output and make sure we have both a person's summoner name and id
        summoner_id = (summoner_response[current_summoner]['id'])
        summoner_name = (summoner_response[current_summoner]['name'])
    
        # NOT USED FOR THIS PROJECT AT THIS TIME
        # Get all of a summoner's mastery data
        #response = api.get_summoner_mastery_data(summoner_id)
        #print (response)
    
        # Get a summoner's top X champion mastery data
        try:
            mastery_response = api.get_top_mastery_data(summoner_id, champs)
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
            lane_response = api.get_champion_role(summoner_id, champList)
            while lane_response == {'status': {'status_code': 429, 'message': '429'}}:
                #print('429 code')
                time.sleep(5)
                lane_response = api.get_champion_role(summoner_id, champList)

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
