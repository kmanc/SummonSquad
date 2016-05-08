import APIConstants as Constants
import requests

class RiotAPI(object):
    
    number = 0
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
        # Get summoner ID for use later
        api_url = Constants.URL['summoner_by_name'].format(
            version=Constants.API_VERSIONS['summoner'],
            names=name
        )
        return self._request_summoner(api_url)
       
    def get_summoner_mastery_data(self, id):
        # Get all summoner mastery data
        api_url = Constants.URL['all_mastery'].format(
            platformId=Constants.PLATFORMS['north_america'],
            playerId=id
        )
        return self._request_mastery(api_url)
        
    def get_top_mastery_data(self, id, champs):
        # Get mastery data for the top X champions, where X is the length of the list 'champs'
        api_url = Constants.URL['top_x_mastery'].format(
            platformId=Constants.PLATFORMS['north_america'],
            playerId=id
        )
        return self._request_top_mastery(api_url, {'count': champs})
        
    def get_champion_role(self, id, champList):
        # Figure out which roles the champion is being played in based off of ranked games
        api_url = Constants.URL['matchlist'].format(
            version=Constants.API_VERSIONS['matchlist'],
            playerId=id
        )
        queues = 'TEAM_BUILDER_DRAFT_RANKED_5x5,RANKED_SOLO_5x5,RANKED_TEAM_5x5'
        champList = ','.join(map(str, champList))
        return self._request_champion_role(api_url, {'championIds': champList, 'rankedQueues': queues})
        
    def get_champion_name(self, champIdizzle):
        # Get champion name from champion ID so we can tell a player they should play 'Thresh', not 'champion 412'
        return self._request_champion_name(champIdizzle)
               
# If request isn't working, check "print (response.url)" first!!!
        