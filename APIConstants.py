URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name':'v{version}/summoner/by-name/{names}',
    'mastery_base':'https://{proxy}.api.pvp.net/{url}',
    'all_mastery':'championmastery/location/{platformId}/player/{playerId}/champions',
    'top_x_mastery':'championmastery/location/{platformId}/player/{playerId}/topchampions',
    'mastery_by_champ':'championmastery/location/{platformId}/player/{playerId}/champion/{championId}',
    'matchlist':'v{version}/matchlist/by-summoner/{playerId}',
    'global_base':'https://global.api.pvp.net/api/lol/static-data/{region}/v{version}/champion/{championId}'
}

API_VERSIONS = {
    'champion': '1.2',
    'matchlist': '2.2',
    'stats': '1.3',
    'summoner': '1.4',
    'global': '1.2'
}

REGIONS = {
    'north_america': 'na',
    'brazil': 'br',
    'eu_nordic': 'eune',
    'eu_west': 'euw',
    'japan': 'jp',
    'korea': 'kr',
    'latin_america_north': 'lan',
    'latin_america_south': 'las',
    'oceania': 'oce',
    'turkey': 'tr',
    'russia': 'ru'
}

PLATFORMS = {
    'north_america': 'NA1',
    'brazil': 'BR1',
    'eu_nordic': 'EUN1',
    'eu_west': 'EUW1',
    'japan': 'JP1',
    'korea': 'KR',
    'latin_america_north': 'LA1',
    'latin_america_south': 'LA2',
    'oceania': 'OC1',
    'turkey': 'TR1',
    'russia': 'RU'
}