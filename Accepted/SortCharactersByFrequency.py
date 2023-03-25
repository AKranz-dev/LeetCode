class Solution:
    def frequencySort(self, s: str) -> str:
        
        letterDict = {}
        returnList = []
        
        for letter in s:
            if letter not in letterDict:
                letterDict[letter] = 1
            else:
                letterDict[letter] +=1

        letterDict = dict(sorted(letterDict.items(), key=lambda item: item[1], reverse=True))
        
        for item in letterDict:
            for i in range(0,letterDict[item]):
                returnList.append(item)
        return returnList




s = "tree"
a = Solution()
print(a.frequencySort(s))