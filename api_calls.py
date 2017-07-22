import api_constants, api_key
import requests

api_key = api_key.key
args = {'api_key': api_key}


def get_region(region):
    return api_constants.REGIONS[region]


def summoner_lookup(summoner_name, region):
    region = get_region(region)
    asset = api_constants.ASSETS['summoner_lookup'].format(version=3, summonerName=summoner_name)
    url = api_constants.URL['base'].format(region=region, asset=asset)
    return requests.get(url, params=args).json()


def champion_mastery(summoner_id, num_champs, region):
    region = get_region(region)
    asset = api_constants.ASSETS['champion_mastery'].format(version=3, summonerId=summoner_id)
    url = api_constants.URL['base'].format(region=region, asset=asset)
    return (requests.get(url, params=args).json())[:num_champs]


def match_history(account_id, champ_list, region):
    region = get_region(region)
    args['champion'] = champ_list
    asset = api_constants.ASSETS['match_history'].format(version=3, accountId=account_id)
    url = api_constants.URL['base'].format(region=region, asset=asset)
    return requests.get(url, params=args).json()


def champion_lookup(region):
    region = get_region(region)
    args['dataById'] = 'true'
    asset = api_constants.ASSETS['champion_lookup'].format(version=3)
    url = api_constants.URL['base'].format(region=region, asset=asset)
    result = requests.get(url, params=args).json()
    return result['data']
