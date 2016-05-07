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
        args = params
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
        
    def _request_champion_role(self, api_url, params={}):
        args = params
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
        return response.json()
        
    def _request_champion_name(self, champIdizzle):
        args = {'api_key': self.api_key}
        response = requests.get(
            Constants.URL['global_base'].format(
                region=Constants.REGIONS['north_america'],
                version=Constants.API_VERSIONS['global'],
                championId=champIdizzle
            ),
            params=args
        )
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
        
    def get_top_mastery_data(self, id, champs):
        api_url = Constants.URL['top_x_mastery'].format(
            platformId=Constants.PLATFORMS['north_america'],
            playerId=id
        )
        return self._request_top_mastery(api_url, {'count': champs})
        
    def get_champion_role(self, id, champList):
        api_url = Constants.URL['matchlist'].format(
            version=Constants.API_VERSIONS['matchlist'],
            playerId=id
        )
        queues = 'TEAM_BUILDER_DRAFT_RANKED_5x5,RANKED_SOLO_5x5,RANKED_TEAM_5x5'
        champList = ','.join(map(str, champList))
        return self._request_champion_role(api_url, {'championIds': champList, 'rankedQueues': queues})
        
    def get_champion_name(self, champIdizzle):
        return self._request_champion_name(champIdizzle)
     
     
     
# If request isn't working, check "print (response.url)" first!!!
        