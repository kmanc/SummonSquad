from RiotAPI import RiotAPI
import json
from GetData import GetData
import sys
from DoMath import DoMath

def main():
    
    # Grab arguments (summoner names) and make sure that they are all there
    try:
        summoners = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
    except:
        sys.exit('At least one summoner name was not entered')
        
    region = sys.argv[6]
    champs = int(sys.argv[7])
    if champs < 5:
        champs = 5
    if champs > 25:
        champs = 25
    
    # Normalize summoner names (no spaces, no upper case) because the api can get cranky if you don't
    for x in range(len(summoners)):
        summoners[x] = summoners[x].lower()
        summoners[x] = summoners[x].replace(" ", "")

    summonerList = []
    data_grabber = GetData()
    computations = DoMath()
    
    # Get a list of the summoners and their respective champion/mastery data
    for player in summoners:
        summoner_data = data_grabber._gimme_data(player, champs, region)
        summonerList.append(summoner_data)

    # Get squad
    # Build the dream
    # ASSSSSSEMBLEEEEEEEEE
    try:
        dream_team = computations._compute_team(summonerList, summoners)
    except:
        sys.exit('You woke up, the dream is gone')
        
    # Output for the website
    print (dream_team)    
    
if __name__ == '__main__':
    main()