class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:

        uniqueUsers = set()
        res = []
        countDict = {}
        trackedDict = {}
        finalDict = {}
        
        #Add all unique users to a dictionary
        for entry in logs:
            uniqueUsers.add(entry[0])
        

        for entry in logs:
            if entry[0] not in countDict:
                countDict[entry[0]] = 1
                trackedDict[entry[0]] = ","+str(entry[1])
            else:
                if str(entry[1]) not in trackedDict[entry[0]]:
                    countDict[entry[0]] += 1
                    trackedDict[entry[0]] += ","+str(entry[1])
        
        #countDict format is {userID: UAM}
       

       #finalDict format is {UAM: Occureneces}
        for entry in countDict:
            if countDict[entry] not in finalDict:
                finalDict[countDict[entry]] = 1
            else:
                finalDict[countDict[entry]] += 1
        print(finalDict)

        for i in range(1,k+1):
            if i not in finalDict:
                res.append(0)
            else:
                res.append(finalDict[i])
        return res



        



logs = [[1,1],[2,2],[2,3]]
k = 4
s = Solution()
print(s.findingUsersActiveMinutes(logs,k))