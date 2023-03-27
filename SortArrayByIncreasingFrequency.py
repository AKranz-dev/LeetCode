class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        
        dictz = {}
        countDict = {}
        returnList = []
        dupeDict = {}
        
        for num in nums:
            if num not in dictz:
                dictz[num] = 1
            else:
                dictz[num] +=1

        dictz = dict(sorted(dictz.items(), key=lambda item: item[1]))

        for item in dictz:
            for i in range(0,dictz[item]):
                returnList.append(item)
        
        for item in dictz:
            if item not in countDict:
                countDict[item] = dictz[item]
            else:
                dupeDict[item] = dictz[item]
        
        print(dupeDict)



        return returnList



nums = [2,3,1,3,2]
s = Solution()
print(s.frequencySort(nums))