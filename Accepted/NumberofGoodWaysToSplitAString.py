class Solution:
    def numSplits(self, s: str) -> int:
        leftDict = {}
        rightDict = {}
        counter = 0


        for letter in s:
            if letter not in rightDict:
                rightDict[letter] = 1
            else:
                rightDict[letter] += 1
        

        
        for letter in s:
            if letter not in leftDict:
                leftDict[letter] = 1
            else:
                leftDict[letter] += 1
            
            rightDict[letter] -= 1
            
            if rightDict[letter] == 0:
                del rightDict[letter]
            
            if len(leftDict) == len(rightDict):
                counter+=1
        
        return counter
                



a = Solution()
s = "aaaaa"
print(a.numSplits(s))