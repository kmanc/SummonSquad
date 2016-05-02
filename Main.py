from RiotAPI import RiotAPI
import json

def main():
    api = RiotAPI('e6e27f9f-d47d-4b3f-96d4-3aab2c2b8cee')
    champs = 10
    data_dict = {}
    champList = []
    second_dict = {}
       
    # Get summoner data
    response = api.get_summoner_by_name('KmancXC')
    
    # Parse the output
    temp = json.dumps(response)
    temp = json.loads(temp)
    summoner_id = (temp['kmancxc']['id'])
    summoner_name = (temp['kmancxc']['name'])
    
    #For troubleshooting
    print (summoner_id, summoner_name)
    
    # Get all of a summoner's mastery data
    #response = api.get_summoner_mastery_data(summoner_id)
    #print (response)
    
    # Get a summoner's top X mastery data
    response = api.get_top_mastery_data(summoner_id, champs)
    
    # Compile the stuff I care about into a dictionary
    for x, val in enumerate(response):
        data_dict[val['championId']] = val['championPoints']
    
    # Find out what lane the champion is being played in
    for key in data_dict:
        champList.append(key)
    response = api.get_champion_role(summoner_id, champList)
    #print (response)
    
    # Process the champion list data
    #print (type(response['matches']))
    for x, val in enumerate(response['matches']):
        second_dict[val['champion']] = val['lane'], val['role']
    print (second_dict)

if __name__ == '__main__':
    main()