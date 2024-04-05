import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        origin = [0,0]
        distList = []
        distDict = {}
        dupeDict = {}
        res = []
        i=0

        #Dictionary key is the distance, and the value is that point
        #Also creating a sorted list of all distances, shortest first
        # for entry in points:
        #     distList.append(math.dist(entry,origin))

        #     if math.dist(entry,origin) in distDict:
        #         dupeDict[math.dist(entry,origin)] = entry
        #     else:
        #         distDict[math.dist(entry,origin)] = entry

        
        # sortedList = sorted(distList)
        
        # print(sortedList)
        # print(distDict) 
        # print("dupeDict: {}".format(dupeDict))

                        # for i in range(k):
                        #     for x in range(len(distList)): #Time limit problem is here - we search every value of the distance list to match the value from the sorted list, temp. This is because we need the index number of that item in the distance list so we know which coordinate to return.
                        #         if sortedList[i] == distList[x] and points[x] not in res:
                        #             res.append(points[x])
                        #             break
        


        # while i < k and len(distDict)>=1:
        #     if sortedList[i] in distDict:
        #         res.append(distDict[sortedList[i]])
        #         distDict.pop(sortedList[i])
        #         print("pop")
        #         i+=1
        #     else:
        #         i+=1

        
        # for item in dupeDict:
        #     if dupeDict[item] in res:
        #         res.append(dupeDict[item])
        #     else:
        #         for entry in res:
        #             if item == math.dist(entry,origin):
        #                 res.append(dupeDict[item])
        #                 break

        # return res


        d = 1

        for entry in points:
            distList.append(math.dist(entry,origin))

            if math.dist(entry,origin) in distDict:
                distDict[(math.dist(entry,origin))] = entry,d
                d+=1
            else:
                distDict[math.dist(entry,origin)] = entry,"x"

        
        sortedList = sorted(distList)
        
        print(sortedList)
        print(distDict) 
        print("dupeDict: {}".format(dupeDict))

        for i in range(k):
            if distDict[sortedList[i]][1] != "x":
                res.append((distDict[sortedList[i]])[0])
            else:
                res.append(distDict[sortedList[i]][0])
        return res





s = Solution()
points = [[0,1],[1,0]]
k = 2
print(s.kClosest(points,k))
