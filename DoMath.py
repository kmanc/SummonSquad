class DoMath(object):
    
    def _compute_team(self, summonerDict):
    
        # A couple of initializations for later use
        self.valid_roles = ['MID', 'TOP', 'JUNGLE', 'DUO_CARRY', 'DUO_SUPPORT']
        best_team_power = -1
        summonerExperienceDict = {}

        # Find total mastery points per summoner (take the total points for each champion, and sum them)    
        for summonerName in summonerDict.keys():
            summonerExperienceDict[summonerName] = 0
            for mastered_champs in summonerDict[summonerName].values():
                for champ_info in mastered_champs.values():
                    for role_info in champ_info.values():
                        for rolescore in role_info.values():
                            summonerExperienceDict[summonerName] += rolescore

        # First we make sure we don't divide by zero at any point down the road           
        for summonerName in summonerExperienceDict.keys():
            if summonerExperienceDict[summonerName] == 0:
                summonerExperienceDict[summonerName] = 1

        # Iterate through team combinations and find the "valid" ones (ones with each of the 5 positions)
        # summonerDict structure
        """
        summoner name:
            summoner id:
                champion id:
                    champion name:
                        role: points
                        role: points
                        role: points
                        ...
                champion id:
                    champion name:
                        role: points
                        ...
                ...
        summoner name:
            ...
        """
        self.teams  = []
        team = []
        self.builder(summonerDict, team)
        print('\nPOST BUILDER\n')
        print(summonerDict)

        if best_team_power > 0:
            return (summoners[0] + ',' + final_champ_zero + ',' + final_role_zero + ',' + summoners[1] + ',' + final_champ_one + ',' + final_role_one + ',' + summoners[2] + ',' + final_champ_two + ','
                                + final_role_two + ',' + summoners[3] + ',' + final_champ_three + ',' + final_role_three + ',' + summoners[4] + ',' + final_champ_four + ',' + final_role_four + ',' 
                                + str(champ_id_array[0]) + ',' + str(champ_id_array[1]) + ',' + str(champ_id_array[2]) + ',' + str(champ_id_array[3]) + ',' + str(champ_id_array[4]))
        else:
            print('There was a failure in DoMath.py')
            if summoner_zero_champ:
                print('Got summoner 0s champ')
            if summoner_one_champ:
                print('Got summoner 1s champ')
            if summoner_two_champ:
                print('Got summoner 2s champ')
            if summoner_three_champ:
                print('Got summoner 3s champ')
            if summoner_four_champ:
                print('Got summoner 4s champ')
            return ('An ideal team could not be found')    

    def builder(self, summonerDict, team):
        for summonerName in summonerDict.keys():
            print('TRYING {}'.format(summonerName))
            for mastered_champs in summonerDict[summonerName].values():
                for champ_info in mastered_champs.values():
                    for role_info in champ_info.values():
                        for role in role_info.keys():
                            print(summonerName, champ_info.keys()[0], role)
                            if summonerName not in team \
                                and champ_info.keys()[0] not in team \
                                and role not in team \
                                and role in self.valid_roles:
                                team.append(summonerName)
                                team.append(champ_info.keys()[0])
                                team.append(role)
                                if len(team) == 15:
                                    print('HEY WE GOT ONE')
                                    print('\t{}'.format(team))
                                    self.teams.append(team)
                                    print('continuing...')
                                    team = team[:-3]
                                    continue
                                print('popping...')
                                summonerDict.pop(summonerName)
                                self.builder(summonerDict, team)