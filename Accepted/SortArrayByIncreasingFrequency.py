class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        
        # dictz = {}
        # countDict = {}
        # returnList = []
        # dupeDict = {}
        
        # for num in nums:
        #     if num not in dictz:
        #         dictz[num] = 1
        #     else:
        #         dictz[num] +=1

        # dictz = dict(sorted(dictz.items(), key=lambda item: item[1]))

        # for item in dictz:
        #     for i in range(0,dictz[item]):
        #         returnList.append(item)
        
        # for item in dictz:
        #     if item not in countDict:
        #         countDict[item] = dictz[item]
        #     else:
        #         dupeDict[item] = dictz[item]
        
        # print(dupeDict)
        
        # return returnList

#====================================================================================================

        countDict = {}
        tempList = []
        returnList = []
        frequencyValues = []
        keyList = []
        countOfDupes = 0

        for num in nums:
            if num not in countDict:
                countDict[num] = 1
            else:
                countDict[num] +=1
        

        #Format: number:frequency
        sortedCountDict = dict(sorted(countDict.items(), key=lambda item: item[1]))
        print(sortedCountDict)
        


        #Create list of the values from the sorted dictionary
        for value in sortedCountDict.values():
            frequencyValues.append(value)

        for item in sortedCountDict:
            keyList.append(item)



        #Iterate through the sorted dictionary of frequencies
        for key in sortedCountDict:
            if countOfDupes > 1:
                countOfDupes -=1
                continue

            #If the current item's frequency appears more than once in the frequencyValues list
            if frequencyValues.count(sortedCountDict[key]) > 1:
                
                #Get count of the number of items that share the same frequency (we know they are next to each other since the dictionary is sorted)
                countOfDupes = frequencyValues.count(sortedCountDict[key])

                #Get the index of the first dupe
                firstDupeIndex = keyList.index(key)

                #Retrieve the current item, and the next X items that have the same frequency and sort them
                for x in range(0,countOfDupes):
                    tempList.append(keyList[firstDupeIndex+x])

                tempList.sort(reverse=True)

                #Check the frequency that all the number share, and add that amount of each to the return list
                amountToAdd = sortedCountDict[tempList[0]]
                for item in tempList:
                    for y in range(amountToAdd):
                        returnList.append(item)
                tempList.clear()
            
            else:
                amountToAdd = sortedCountDict[key]
                for z in range(amountToAdd):
                    returnList.append(key)

        return returnList

                



nums = [-1,1,-6,4,5,-6,1,4,1]
s = Solution()
print(s.frequencySort(nums))