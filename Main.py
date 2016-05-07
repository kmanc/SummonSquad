from RiotAPI import RiotAPI
import json
from GetData import GetData
import sys
from DoMath import DoMath

def main():
    
    # This will likely get moved to a user-entered variable instead of hard coded
    champs = 15
    
    # Grab arguments and make sure that they are all there
    try:
        summoners = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
    except:
        sys.exit('At least one summoner name was not entered')
    
    for x in range(len(summoners)):
        summoners[x] = summoners[x].lower()
        summoners[x] = summoners[x].replace(" ", "")

    summonerList = []
    data_grabber = GetData()
    computations = DoMath()
    
    # Get a list of the summoners and their respective champion/mastery data, or return error if something goes wrong
    for player in summoners:
        try:
            summoner_data = data_grabber._gimme_data(player, champs)
        except:
            sys.exit('Summoner name does not exist')
        summonerList.append(summoner_data)

    # Get squad
    dream_team = computations._compute_team(summonerList, summoners)
    
    # Output for the website
    print (dream_team)    
    
if __name__ == '__main__':
    main()