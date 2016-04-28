import APIConstants as Constants
import requests

class RiotAPI(object):
    
    def __init__(self, api_key, region=Constants.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        print ('FUCKO')
        response = requests.get(
            Constants.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
            ),
            params=args,
        )
        print ('FUCKO 2')
        print (response.url)
        return response.json()
        
    def get_summoner_by_name(self, name):
        api_url = Constants.URL['summoner_by_name'].format(
            version=Constants.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)
        