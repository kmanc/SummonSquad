from RiotAPI import RiotAPI
import json
import operator
from GetData import GetData

def main():
    
    summoners = ['Kmancxc','berkfleriosa']
    for x in range(len(summoners)):
        summoners[x] = summoners[x].lower()

    myList = []
    data_grabber = GetData()
    for player in summoners:
        summoner_data = data_grabber._gimme_data(player)
        myList.append(summoner_data)
    for x in range(len(myList)):
        print (myList[x])
    
if __name__ == '__main__':
    main()