import APIConstants, KeyAPI
import requests

api_key = KeyAPI.key
args = {'api_key': api_key}


def get_region(region):
    return APIConstants.REGIONS[region]


def summoner_lookup(summoner_name, region):
    region = get_region(region)
    asset = APIConstants.ASSETS['summoner_lookup'].format(version=3, summonerName=summoner_name)
    url = APIConstants.URL['base'].format(region=region, asset=asset)
    return requests.get(url, params=args).json()


def champion_mastery(summoner_id, num_champs, region):
    region = get_region(region)
    asset = APIConstants.ASSETS['champion_mastery'].format(version=3, summonerId=summoner_id)
    url = APIConstants.URL['base'].format(region=region, asset=asset)
    return (requests.get(url, params=args).json())[:num_champs]


def match_history(account_id, champ_list, region):
    region = get_region(region)
    args['champion'] = champ_list
    asset = APIConstants.ASSETS['match_history'].format(version=3, accountId=account_id)
    url = APIConstants.URL['base'].format(region=region, asset=asset)
    return requests.get(url, params=args).json()


def champion_lookup(region):
    region = get_region(region)
    args['dataById'] = 'true'
    asset = APIConstants.ASSETS['champion_lookup'].format(version=3)
    url = APIConstants.URL['base'].format(region=region, asset=asset)
    result = requests.get(url, params=args).json()
    return result['data']
