from RiotAPI import RiotAPI
import json
import operator
from GetData import GetData

def main():
    
    summoners = ['Kmancxc', 'berkfleriosa']
    for x in range(len(summoners)):
        summoners[x] = summoners[x].lower()

    summonerList = []
    data_grabber = GetData()
    for player in summoners:
        summoner_data = data_grabber._gimme_data(player)
        summonerList.append(summoner_data)
    
    for summoner in range(len(summonerList)):
        #print (summonerList[summoner])
        for x, mastered_champs in summonerList[summoner].items():
            #print (mastered_champs)
            for x, champ_info in mastered_champs.items():
                #print (champ_info[1:])
                for role_info in champ_info[1:]:
                    #print (role_info)
                    for role in role_info:
                        print (role)
    
if __name__ == '__main__':
    main()