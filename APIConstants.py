URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'mastery_base':'https://{proxy}.api.pvp.net/',
    'all_mastery':'championmastery/location/{platformId}/player/{playerId}/champions',
    'mastery_by_champ':'championmastery/location/{platformId}/player/{playerId}/champion/{championId}',
}

API_VERSIONS = {
    'champion': '1.2',
    'championmastery': '',
    'stats': '1.3',
    'summoner': '1.4'
}

REGIONS = {
    'north_america': 'na'
}

PLATFORMS = {
    'north_america': 'NA1'
}