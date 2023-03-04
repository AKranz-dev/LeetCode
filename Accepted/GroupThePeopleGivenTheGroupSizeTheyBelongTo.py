class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:

        dict = {}
        currentList = []
        returnList = []
        lastIndex = 0


        for groupsize in groupSizes:
            if groupsize not in dict:
                dict[groupsize] = 1
            else:
                dict[groupsize] +=1

  

        for entry in dict:
            totalGroups = dict[entry]/entry
            lastIndex = 0
            for i in range(0,int(totalGroups)):
                currentList.clear()
                for i in range(0,entry):
                    print("Appending {} to the list...".format(groupSizes.index(entry,lastIndex)))
                    currentList.append(groupSizes.index(entry,lastIndex))
                    lastIndex = groupSizes.index(entry,lastIndex)+1
                print("Adding current List {} to the return list...".format(currentList))
                returnList.append(currentList[:])
                print(returnList)
        return returnList
                







s = Solution()
groupSizes = [3,3,3,3,3,1,3]
print(s.groupThePeople(groupSizes))