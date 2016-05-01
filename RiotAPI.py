import APIConstants as Constants
import requests

class RiotAPI(object):
    
    def __init__(self, api_key, region=Constants.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region
        
    def _request_summoner(self, api_url, params={}):
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
        
    def _request_mastery(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Constants.URL['mastery_base'].format(
                proxy=self.region,
                url=api_url
            ),
            params=args
        )
        return response.json()
        
    def _request_top_mastery(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Constants.URL['mastery_base'].format(
                proxy=self.region,
                url=api_url
            ),
            params=args
        )
        print (args)
        print (response.url)
        return response.json()
        
    def get_summoner_by_name(self, name):
        api_url = Constants.URL['summoner_by_name'].format(
            version=Constants.API_VERSIONS['summoner'],
            names=name
        )
        return self._request_summoner(api_url)
       
    def get_summoner_mastery_data(self, id):
        api_url = Constants.URL['all_mastery'].format(
            platformId=Constants.PLATFORMS['north_america'],
            playerId=id
        )
        return self._request_mastery(api_url)
        
    def get_top_mastery_data(self, id):
        api_url = Constants.URL['top_x_mastery'].format(
            platformId=Constants.PLATFORMS['north_america'],
            playerId=id
        )
        return self._request_top_mastery(api_url, {'count': 'count=10'})
     
        