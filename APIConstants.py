URL = {
    'base': 'https://{region}.api.riotgames.com/{asset}',
}

ASSETS = {
    'champion_mastery': '/lol/champion-mastery/v{version}/champion-masteries/by-summoner/{summonerId}',
    'summoner_lookup': '/lol/summoner/v{version}/summoners/by-name/{summonerName}',
    'match_history': '/lol/match/v{version}/matchlists/by-account/{accountId}',
    'champion_lookup': '/lol/static-data/v{version}/champions',
}

REGIONS = {
    'NA': 'na1',
    'BR': 'br1',
    'EUN': 'eun1',
    'EUW': 'euw1',
    'JP': 'jp1',
    'KR': 'kr',
    'LAN': 'la1',
    'LAS': 'la2',
    'OC': 'oc1',
    'TR': 'tr1',
    'RU': 'ru'
}