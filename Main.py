from RiotAPI import RiotAPI
import json

def main():
    api = RiotAPI('e6e27f9f-d47d-4b3f-96d4-3aab2c2b8cee')
    champs = 10
    data_dict = {}
    champList = []
    second_dict = {}
    champIdizzle = 11
    class MyStruct():
    def __init__(self, championId=0, championRole='unknown', championPoints=0):
        self.championId = championId
        self.championRole = championRole
        self.championRole = championPoints
       
    # Get summoner data
    summoner_response = api.get_summoner_by_name('KmancXC')
    
    # Parse the output
    temp = json.dumps(summoner_response)
    temp = json.loads(temp)
    summoner_id = (temp['kmancxc']['id'])
    summoner_name = (temp['kmancxc']['name'])
    
    #For troubleshooting
    print (summoner_id, summoner_name)
    
    # Get all of a summoner's mastery data
    #response = api.get_summoner_mastery_data(summoner_id)
    #print (response)
    
    # Get a summoner's top X mastery data
    mastery_response = api.get_top_mastery_data(summoner_id, champs)
    
    # Compile the stuff I care about into a dictionary
    for x, val in enumerate(mastery_response):
        data_dict[val['championId']] = val['championPoints']
    
    # Find out what lane the champion is being played in
    for key in data_dict:
        champList.append(key)
    lane_response = api.get_champion_role(summoner_id, champList)
    
    # Process the champion list data
    #print (type(response['matches']))
    for x, val in enumerate(lane_response['matches']):
        second_dict[val['champion']] = val['lane'], val['role']
    
    combined_dict = {}
    for key in (data_dict.keys() | second_dict.keys()):
        if key in data_dict: combined_dict.setdefault(key, []).append(data_dict[key])
        if key in second_dict: combined_dict.setdefault(key, []).append(second_dict[key])
    
    # Get the champion name for later use
    champion_response = api.get_champion_name(champIdizzle)
    champion_name = champion_response['name']
    
    champion_name = MyStruct()
    

if __name__ == '__main__':
    main()