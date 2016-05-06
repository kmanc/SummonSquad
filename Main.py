from RiotAPI import RiotAPI
import json
from GetData import GetData
import sys
from DoMath import DoMath

def main():
    
    summoners = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
    
    for x in range(len(summoners)):
        summoners[x] = summoners[x].lower()
        summoners[x] = summoners[x].replace(" ", "")

    summonerList = []
    data_grabber = GetData()
    computations = DoMath()
    
    # Get a list of the summoners and their respective champion/mastery data
    for player in summoners:
        summoner_data = data_grabber._gimme_data(player)
        summonerList.append(summoner_data)

    dream_team = computations._compute_team(summonerList, summoners)
    
    print (dream_team)    
    
if __name__ == '__main__':
    main()