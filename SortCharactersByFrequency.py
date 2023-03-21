class Solution:
    def frequencySort(self, s: str) -> str:
        
        letterDict = {}
        
        for letter in s:
            if letter not in letterDict:
                letterDict[letter] = 1
            else:
                letterDict[letter] +=1
        print(letterDict)

        #sort dictionary by value, iterate through dictionary keys and append to a list, return the list.





s = "tree"
a = Solution()
print(a.frequencySort(s))