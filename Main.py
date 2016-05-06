from RiotAPI import RiotAPI
import json
import operator
from GetData import GetData
import sys

def main():
    
    #summoners = ['Kmancxc', 'berkfleriosa', 'Corduroys', 'AshtreeLee', 'fierce invalid']
    summoners = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
    for x in range(len(summoners)):
        summoners[x] = summoners[x].lower()
        summoners[x] = summoners[x].replace(" ", "")

    summonerList = []
    data_grabber = GetData()
    for player in summoners:
        summoner_data = data_grabber._gimme_data(player)
        summonerList.append(summoner_data)
        
    for x0, mastered_champs0 in summonerList[0].items():
        #print (mastered_champs1)
        for x0, champ_info0 in mastered_champs0.items():
                #print (champ_info1[1:])
                for role_info0 in champ_info0[1:]:
                    #print (role_info0)
                    for role0 in role_info0:
                        #print ('summoner 0', x0, role0)
                        roleList = []
                        champList = []
                        summoner_zero_role = role0
                        summoner_zero_champ = x0
                        if (summoner_zero_role == 'NONE' or summoner_zero_role == 'DUO'):
                            continue
                        roleList.append(summoner_zero_role)
                        champList.append(summoner_zero_champ)
                        for x1, mastered_champs1 in summonerList[1].items():
                            #print (mastered_champs1)
                            for x1, champ_info1 in mastered_champs1.items():
                                #print (champ_info1[1:])
                                for role_info1 in champ_info1[1:]:
                                    #print (role_info1)
                                    for role1 in role_info1:
                                        #print ('summoner 1', x1, role1)
                                        summoner_one_role = role1
                                        summoner_one_champ = x1
                                        if (summoner_one_role == 'NONE' or summoner_one_role == 'DUO' or summoner_one_role in roleList or len(roleList) == 0 or summoner_one_champ in champList):
                                            continue
                                        roleList.append(summoner_one_role)
                                        champList.append(summoner_one_champ)
                                        #print (roleList)
                                        for x2, mastered_champs2 in summonerList[2].items():
                                            #print (mastered_champs2)
                                            for x2, champ_info2 in mastered_champs2.items():
                                                #print (champ_info2[1:])
                                                for role_info2 in champ_info2[1:]:
                                                    #print (role_info2)
                                                    for role2 in role_info2:
                                                        #print ('summoner 2', x2, role2)
                                                        summoner_two_role = role2
                                                        summoner_two_champ = x2
                                                        if (summoner_two_role == 'NONE' or summoner_two_role == 'DUO' or summoner_two_role in roleList or len(roleList) <= 1 or summoner_two_champ in champList):
                                                            continue
                                                        roleList.append(summoner_two_role)
                                                        champList.append(summoner_two_champ)
                                                        for x3, mastered_champs3 in summonerList[3].items():
                                                            #print (mastered_champs3)
                                                            for x3, champ_info3 in mastered_champs3.items():
                                                                #print (champ_info3[1:])
                                                                for role_info3 in champ_info3[1:]:
                                                                    #print (role_info3)
                                                                    for role3 in role_info3:
                                                                        #print ('summoner 3', x3, role3)
                                                                        summoner_three_role = role3
                                                                        summoner_three_champ = x3
                                                                        if (summoner_three_role == 'NONE' or summoner_three_role == 'DUO' or summoner_three_role in roleList or len(roleList) <= 2 or summoner_three_champ in champList):
                                                                            continue
                                                                        champList.append(summoner_three_champ)
                                                                        roleList.append(summoner_three_role)
                                                                        for x4, mastered_champs4 in summonerList[4].items():
                                                                            #print (mastered_champs4)
                                                                            for x4, champ_info4 in mastered_champs4.items():
                                                                                #print (champ_info4[1:])
                                                                                for role_info4 in champ_info4[1:]:
                                                                                    #print (role_info4)
                                                                                    for role4 in role_info4:
                                                                                        #print ('summoner 4', x4, role4)
                                                                                        summoner_four_role = role4
                                                                                        summoner_four_champ = x4
                                                                                        if (summoner_four_role == 'NONE' or summoner_four_role == 'DUO' or summoner_four_role in roleList or len(roleList) <= 3 or summoner_four_champ in champList):
                                                                                            continue
                                                                                        else:
                                                                                            roleList = []
                                                                                            print ('valid team found')
                                                                                            print (summoner_zero_champ, summoner_zero_role)
                                                                                            print (summoner_one_champ, summoner_one_role)
                                                                                            print (summoner_two_champ, summoner_two_role)
                                                                                            print (summoner_three_champ, summoner_three_role)
                                                                                            print (summoner_four_champ, summoner_four_role)
                                                                                            print ()
    
    
if __name__ == '__main__':
    main()