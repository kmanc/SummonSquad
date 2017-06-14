import NewAPIConstants as Constants
import KeyAPI
import requests

api_key = KeyAPI.key
args = {'api_key': api_key}


def get_region(region):
    return Constants.REGIONS[region]


def summoner_lookup(summoner_name, region):
    region = get_region(region)
    asset = Constants.ASSETS['summoner_lookup'].format(version=3, summonerName=summoner_name)
    url = Constants.URL['base'].format(region=region, asset=asset)
    return requests.get(url, params=args).json()


def champion_mastery(summoner_id, region, num_champs):
    region = get_region(region)
    asset = Constants.ASSETS['champion_mastery'].format(version=3, summonerId=summoner_id)
    url = Constants.URL['base'].format(region=region, asset=asset)
    return (requests.get(url, params=args).json())[:num_champs]


def match_history(account_id, region, champ_list):
    region = get_region(region)
    args['champion'] = champ_list
    asset = Constants.ASSETS['match_history'].format(version=3, accountId=account_id)
    url = Constants.URL['base'].format(region=region, asset=asset)
    return requests.get(url, params=args).json()


def champion_lookup(region):
    region = get_region(region)
    args['dataById'] = 'true'
    asset = Constants.ASSETS['champion_lookup'].format(version=3)
    url = Constants.URL['base'].format(region=region, asset=asset)
    result = requests.get(url, params=args).json()
    return result['data']
