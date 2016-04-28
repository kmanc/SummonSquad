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
        response = requests.get(
            Constants.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
            ),
            params=args
        )
        #print (response.url)
        return response.json()
        
    def _requestTwo(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Constants.URL['mastery_base'].format(
                proxy=self.region
            ),
            params=args
        )
        #print (response.url)
        return response.json()
        
    def get_summoner_by_name(self, name):
        api_url = Constants.URL['summoner_by_name'].format(
            version=Constants.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)
       
    def get_summoner_mastery_data(self, id):
        api_url = Constants.URL['all_mastery'].format(
            platformId=Constants.API_PLATFORMS['north_america'],
            playerId=id
        )
        return self._requestTwo(api_url)
     
        