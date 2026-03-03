class Solution:
    def balancedStringSplit(self, s: str) -> int:

        letDict = {}
        counter = 0


        for letter in s:
            
            
            if letter not in letDict:
                letDict[letter] = 1
            else:
                letDict[letter] +=1
        

            if len(letDict)>1 and letDict["L"] == letDict["R"]:
                counter +=1
                letDict = {}
        
        return counter

a = Solution()
s = "RLRRLLRLRL"
print(a.balancedStringSplit(s))