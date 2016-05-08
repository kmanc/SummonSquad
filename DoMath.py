class DoMath(object):
    
    def _compute_team(self, summonerList, summoners):
    
        total_mastery0 = total_mastery1 = total_mastery2 = total_mastery3 = total_mastery4 = 0
        specific_mastery0 = specific_mastery1 = specific_mastery2 = specific_mastery3 = specific_mastery4 = 0
        current_team_power = 0
        best_team_power = -1
        final_champ_zero = final_champ_one = final_champ_two = final_champ_three = final_champ_four = ''
        final_role_zero = final_role_one = final_role_two = final_role_three = final_role_four = ''
        valid_roles = ['MID', 'TOP', 'JUNGLE', 'DUO_CARRY', 'DUO_SUPPORT']
        
        # Find total mastery points per summoner    
        for x0, mastered_champs0 in summonerList[0].items():
            for x0, champ_info0 in mastered_champs0.items():
                for role_info0 in champ_info0[1:]:
                    total_mastery0 += int(list(role_info0.values())[0])
    
        for x1, mastered_champs1 in summonerList[1].items():
            for x1, champ_info1 in mastered_champs1.items():
                for role_info1 in champ_info1[1:]:
                    total_mastery1 += int(list(role_info1.values())[0])
       
        for x2, mastered_champs2 in summonerList[2].items():
            for x2, champ_info2 in mastered_champs2.items():
                for role_info2 in champ_info2[1:]:
                    total_mastery2 += int(list(role_info2.values())[0])
       
        for x3, mastered_champs3 in summonerList[3].items():
            for x3, champ_info3 in mastered_champs3.items():
                for role_info3 in champ_info3[1:]:
                    total_mastery3 += int(list(role_info3.values())[0])
        
        for x4, mastered_champs4 in summonerList[4].items():
            for x4, champ_info4 in mastered_champs4.items():
                for role_info4 in champ_info4[1:]:
                    total_mastery4 += int(list(role_info4.values())[0])

        # Iterate through team combinations and find the "valid" ones (ones with each of the 5 positions)
        # Is it efficient?  Probably not, but time conquers all
        for x0, mastered_champs0 in summonerList[0].items():
            #print (mastered_champs0)
            for x0, champ_info0 in mastered_champs0.items():
                    #print (champ_info0[1:])
                    #print (champ_info0[:1])
                    #print (champList, 'reset 1')
                    for role_info0 in champ_info0[1:]:
                        #print (role_info0)
                        for role0 in role_info0:
                            #print ('summoner 0', x0, role0)
                            roleList = []
                            champList = []
                            summoner_zero_role = role0
                            summoner_zero_champ = x0
                            summoner_zero_champ_name = champ_info0[:1]
                            if (summoner_zero_role not in valid_roles):
                                continue
                            roleList.append(summoner_zero_role)
                            champList.append(summoner_zero_champ)
                            for x1, mastered_champs1 in summonerList[1].items():
                                for x1, champ_info1 in mastered_champs1.items():
                                    #champList = champList[:1]
                                    for role_info1 in champ_info1[1:]:
                                        for role1 in role_info1:
                                            roleList = roleList[:1]
                                            champList = champList[:1]
                                            summoner_one_role = role1
                                            summoner_one_champ = x1
                                            summoner_one_champ_name = champ_info1[:1]
                                            if (summoner_one_role not in valid_roles or summoner_one_role in roleList or len(roleList) == 0 or summoner_one_champ in champList):
                                                continue
                                            roleList.append(summoner_one_role)
                                            champList.append(summoner_one_champ)
                                            for x2, mastered_champs2 in summonerList[2].items():
                                                for x2, champ_info2 in mastered_champs2.items():
                                                    for role_info2 in champ_info2[1:]:
                                                        for role2 in role_info2:
                                                            roleList = roleList[:2]
                                                            champList = champList[:2]
                                                            summoner_two_role = role2
                                                            summoner_two_champ = x2
                                                            summoner_two_champ_name = champ_info2[:1]
                                                            if (summoner_two_role not in valid_roles or summoner_two_role in roleList or len(roleList) <= 1 or summoner_two_champ in champList):
                                                                continue
                                                            roleList.append(summoner_two_role)
                                                            champList.append(summoner_two_champ)
                                                            for x3, mastered_champs3 in summonerList[3].items():
                                                                for x3, champ_info3 in mastered_champs3.items():
                                                                    for role_info3 in champ_info3[1:]:
                                                                        for role3 in role_info3:
                                                                            roleList = roleList[:3]
                                                                            champList = champList[:3]
                                                                            summoner_three_role = role3
                                                                            summoner_three_champ = x3
                                                                            summoner_three_champ_name = champ_info3[:1]
                                                                            if (summoner_three_role not in valid_roles or summoner_three_role in roleList or len(roleList) <= 2 or summoner_three_champ in champList):
                                                                                continue
                                                                            champList.append(summoner_three_champ)
                                                                            roleList.append(summoner_three_role)
                                                                            for x4, mastered_champs4 in summonerList[4].items():
                                                                                for x4, champ_info4 in mastered_champs4.items():
                                                                                    for role_info4 in champ_info4[1:]:
                                                                                        for role4 in role_info4:
                                                                                            roleList = roleList[:4]
                                                                                            champList = champList[:4]
                                                                                            summoner_four_role = role4
                                                                                            summoner_four_champ = x4
                                                                                            summoner_four_champ_name = champ_info4[:1]
                                                                                            if (summoner_four_role not in valid_roles or summoner_four_role in roleList or len(roleList) <= 3 or summoner_four_champ in champList):
                                                                                                continue
                                                                                            else:
                                                                                                champList.append(summoner_four_champ)
                                                                                                roleList.append(summoner_four_role)
                                                                                                # Do math to see if the team should be played
                                                                                                if total_mastery0 == 0:
                                                                                                    total_mastery0 = 1
                                                                                                if total_mastery1 == 0:
                                                                                                    total_mastery1 = 1
                                                                                                if total_mastery2 == 0:
                                                                                                    total_mastery2 = 1
                                                                                                if total_mastery3 == 0:
                                                                                                    total_mastery3 = 1
                                                                                                if total_mastery4 == 0:
                                                                                                    total_mastery4 = 1
                                                                                                specific_mastery0 = int(list(role_info0.values())[0]) / total_mastery0
                                                                                                specific_mastery1 = int(list(role_info1.values())[0]) / total_mastery1
                                                                                                specific_mastery2 = int(list(role_info2.values())[0]) / total_mastery2
                                                                                                specific_mastery3 = int(list(role_info3.values())[0]) / total_mastery3
                                                                                                specific_mastery4 = int(list(role_info4.values())[0]) / total_mastery4
                                                                                                current_team_power = specific_mastery0 + specific_mastery1 + specific_mastery2 + specific_mastery3 + specific_mastery4
                                                                                                if current_team_power > best_team_power:
                                                                                                    best_team_power = current_team_power
                                                                                                    final_champ_zero = str(summoner_zero_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_one = str(summoner_one_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_two = str(summoner_two_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_three = str(summoner_three_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_four = str(summoner_four_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '"')
                                                                                                    final_role_zero = str(summoner_zero_role)
                                                                                                    final_role_one = str(summoner_one_role)
                                                                                                    final_role_two = str(summoner_two_role)
                                                                                                    final_role_three = str(summoner_three_role)
                                                                                                    final_role_four = str(summoner_four_role)

        return (summoners[0] + ',' + final_champ_zero + ',' + final_role_zero + ',' + summoners[1] + ',' + final_champ_one + ',' + final_role_one + ',' + summoners[2] + ',' + final_champ_two + ','
                             + final_role_two + ',' + summoners[3] + ',' + final_champ_three + ',' + final_role_three + ',' + summoners[4] + ',' + final_champ_four + ',' + final_role_four)                                                                                   