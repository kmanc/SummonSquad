import api_constants, api_key
import requests, os, json

region = 'na1'
api_key = api_key.key
args = {'api_key': api_key}

dir_path = os.path.dirname(os.path.realpath(__file__))
champ_file = '{0}/{1}'.format(dir_path, 'champion_dict.json')
args['dataById'] = 'true'
asset = api_constants.ASSETS['champion_lookup'].format(version=3)
url = api_constants.URL['base'].format(region=region, asset=asset)
result = requests.get(url, params=args).json()
with open(champ_file, 'w') as f:
    f.write(json.dumps(result['data']))
