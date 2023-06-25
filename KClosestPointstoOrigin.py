import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        origin = [0,0]
        distList = []
        distDict = {}
        res = []


        for entry in points:
            distList.append(math.dist(entry,origin))
            distDict[math.dist(entry,origin)] = entry

        
        sortedList = sorted(distList)
        
        print(distDict) 
        print(sortedList)

        # for i in range(k):
        #     for x in range(len(distList)): #Time limit problem is here - we search every value of the distance list to match the value from the sorted list, temp. This is because we need the index number of that item in the distance list so we know which coordinate to return.
        #         if sortedList[i] == distList[x] and points[x] not in res:
        #             res.append(points[x])
        #             break


        # for i in range(k):
        #     if distDict[sortedList[i]] in res:
        #         distDict.pop(sortedList[i])
        #         res.append(distDict[sortedList[i]])
        #     else:
        #         res.append(distDict[sortedList[i]])


        
        return res








s = Solution()
points = [[2,2],[2,2],[3,3],[2,-2],[1,1]]
k = 4
print(s.kClosest(points,k))
