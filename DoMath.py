class DoMath(object):
    
    def _compute_team(self, summonerDict):
    
        # A couple of initializations for later use
        self.valid_roles = ['MID', 'TOP', 'JUNGLE', 'DUO_CARRY', 'DUO_SUPPORT']
        self.summonerExperienceDict = {}
        #self.summonerOrder = []

        # Find total mastery points per summoner (take the total points for each champion, and sum them)    
        for summonerInfo in summonerDict.keys():
            #self.summonerOrder.append(summonerInfo)
            self.summonerExperienceDict[summonerInfo[0]] = 0
            for champInfo in summonerDict[summonerInfo].keys():
                for champRole in summonerDict[summonerInfo][champInfo].keys():
                    self.summonerExperienceDict[summonerInfo[0]] += summonerDict[summonerInfo][champInfo][champRole]

        # First we make sure we don't divide by zero at any point down the road           
        for summonerName in self.summonerExperienceDict.keys():
            if self.summonerExperienceDict[summonerName] == 0:
                self.summonerExperienceDict[summonerName] = 1

        # Iterate through team combinations and find the "valid" ones (ones with each of the 5 positions)
        # summonerDict structure
        """
        summoner name, summoner id:
            champion name, champion id:
                role: points
                role: points
                role: points
                ...
            champion name, champion id:
                role: points
                ...
            ...
        summoner name, summoner id:
            ...
        """
        self.teamChamps  = []
        self.teamRoles = []
        #self.champScores = []
        #self.teamString = ''
        self.bestScore = -1
        outString = self.builder(summonerDict)
        #self.recursiveBuilder(summonerDict, self.summonerOrder.pop())
        #print(self.teamString)
        return outString

    def builder(self, summonerDict):
        keyList = list(summonerDict.keys())
        summoner0 = keyList[0]
        summoner1 = keyList[1]
        summoner2 = keyList[2]
        summoner3 = keyList[3]
        summoner4 = keyList[4]
        # Summoner 0
        for champs0 in summonerDict[summoner0]:
            self.teamChamps = []
            # Add the champion to the champ list
            self.teamChamps.append(champs0[0])
            for roles0 in summonerDict[summoner0][champs0]:
                self.teamRoles = []
                # Check to see if we have a valid role
                if roles0 not in self.valid_roles:
                    continue
                # Add the tole to the role list
                self.teamRoles.append(roles0)
                for champs1 in summonerDict[summoner1]:
                    self.teamChamps = self.teamChamps[:1]
                    if champs1[0] in self.teamChamps:
                        continue
                    self.teamChamps.append(champs1[0])
                    for roles1 in summonerDict[summoner1][champs1]:
                        self.teamRoles = self.teamRoles[:1]
                        if roles1 not in self.valid_roles or roles1 in self.teamRoles:
                            continue
                        self.teamRoles.append(roles1)
                        for champs2 in summonerDict[summoner2]:
                            self.teamChamps = self.teamChamps[:2]
                            if champs2[0] in self.teamChamps:
                                continue
                            self.teamChamps.append(champs2[0])
                            for roles2 in summonerDict[summoner2][champs2]:
                                self.teamRoles = self.teamRoles[:2]
                                if roles2 not in self.valid_roles or roles2 in self.teamRoles:
                                    continue
                                self.teamRoles.append(roles2)  
                                for champs3 in summonerDict[summoner3]:
                                    self.teamChamps = self.teamChamps[:3]
                                    if champs3[0] in self.teamChamps:
                                        continue
                                    self.teamChamps.append(champs3[0])
                                    for roles3 in summonerDict[summoner3][champs3]:
                                        self.teamRoles = self.teamRoles[:3]
                                        if roles3 not in self.valid_roles or roles3 in self.teamRoles:
                                            continue
                                        self.teamRoles.append(roles3)
                                        for champs4 in summonerDict[summoner4]:
                                            self.teamChamps = self.teamChamps[:4]
                                            if champs4[0] in self.teamChamps:
                                                continue
                                            self.teamChamps.append(champs4[0])
                                            for roles4 in summonerDict[summoner4][champs4]:
                                                self.teamRoles = self.teamRoles[:4]
                                                if roles4 not in self.valid_roles or roles4 in self.teamRoles:
                                                    continue
                                                self.teamRoles.append(roles4)
                                                #####################################    
                                                #####################################
                                                #           WE GOT A TEAM           #
                                                #####################################
                                                #####################################
                                                summoner0Points = summonerDict[summoner0][champs0][roles0] / self.summonerExperienceDict[summoner0[0]]
                                                summoner1Points = summonerDict[summoner1][champs1][roles1] / self.summonerExperienceDict[summoner1[0]] 
                                                summoner2Points = summonerDict[summoner2][champs2][roles2] / self.summonerExperienceDict[summoner2[0]] 
                                                summoner3Points = summonerDict[summoner3][champs3][roles3] / self.summonerExperienceDict[summoner3[0]]
                                                summoner4Points = summonerDict[summoner4][champs4][roles4] / self.summonerExperienceDict[summoner4[0]]
                                                currentTeamPower = summoner0Points + summoner1Points + summoner2Points + summoner3Points + summoner4Points
                                                if currentTeamPower > self.bestScore:
                                                    self.bestScore = currentTeamPower
                                                    idealChamp0 = champs0[0]
                                                    idealChamp0Id = champs0[1]
                                                    idealRole0 = roles0
                                                    idealChamp1 = champs1[0]
                                                    idealChamp1Id = champs1[1]
                                                    idealRole1 = roles1 
                                                    idealChamp2 = champs2[0]
                                                    idealChamp2Id = champs2[1]
                                                    idealRole2 = roles2 
                                                    idealChamp3 = champs3[0]
                                                    idealChamp3Id = champs3[1]
                                                    idealRole3 = roles3 
                                                    idealChamp4 = champs4[0]
                                                    idealChamp4Id = champs4[1]
                                                    idealRole4 = roles4

        if self.bestScore > 0:
            return ('{0},{1},{2},'
                    '{3},{4},{5},'
                    '{6},{7},{8},'
                    '{9},{10},{11},'
                    '{12},{13},{14},'
                    '{15},{16},{17},{18},{19}'.format(
                         summoner0[0], idealChamp0, idealRole0,
                         summoner1[0], idealChamp1, idealRole1,
                         summoner2[0], idealChamp2, idealRole2,
                         summoner3[0], idealChamp3, idealRole3,
                         summoner4[0], idealChamp4, idealRole4,
                         idealChamp0Id, idealChamp1Id, idealChamp2Id,
                         idealChamp3Id, idealChamp4Id))
        else:
            return 'An ideal team was not found'

"""    def recursiveBuilder(self, summonerDict, summoner):
        for champs in summonerDict[summoner]:
            if champs[0] in self.teamChamps:
                continue
            self.teamChamps.append(champs[0])
            print('c')
            for role in summonerDict[summoner][champs]:
                print('e')
                if role not in self.valid_roles or role in self.teamRoles:
                    continue
                self.teamRoles.append(role)
                print('a')
                self.champScores.append(summonerDict[summoner][champs][roles] / 
                                        self.summonerExperienceDict[summoner])
                if len(self.teamRoles) == 5 and len(self.teamChamps) == 5 and len(self.champScores) == 5:
                    if sum(self.champScores) > self.bestScore:
                        self.bestScore = sum(champScores)
                        self.teamString = ('{0},{1},{2},'
                                           '{3},{4},{5},'
                                           '{6},{7},{8},'
                                           '{9},{10},{11},'
                                           '{12},{13},{14},'
                                           '{15},{16},{17}'.format(
                                            self.summonerOrder[0], self.teamChamps[0], self.teamRoles[0],
                                            self.summonerOrder[1], self.teamChamps[1], self.teamRoles[1],
                                            self.summonerOrder[2], self.teamChamps[2], self.teamRoles[2],
                                            self.summonerOrder[3], self.teamChamps[3], self.teamRoles[3],
                                            self.summonerOrder[4], self.teamChamps[4], self.teamRoles[4]))
                else:
                    recursiveBuilder(summonerDict, self.summonerOrder.pop())"""
