from RiotAPI import RiotAPI
import json

def main():
    api = RiotAPI('e6e27f9f-d47d-4b3f-96d4-3aab2c2b8cee')
    
    # Get summoner data
    response = api.get_summoner_by_name('KmancXC')
    print (response)
    
    # Parse the output
    temp = json.dumps(response)
    temp = json.loads(temp)
    summoner_id = (temp['kmancxc']['id'])
    summoner_name = (temp['kmancxc']['name'])
    print (summoner_id, summoner_name)
    
    # Get summoner's mastery data
    response = api.get_summoner_mastery_data(summoner_id)
    #print (response)
    
    # Get summoner's top X mastery data
    response = api.get_top_mastery_data(summoner_id)
    print (response)

if __name__ == '__main__':
    main()