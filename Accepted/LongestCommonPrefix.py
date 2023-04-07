#https://leetcode.com/problems/longest-common-prefix/solutions/?languageTags=python3

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:        
        
        
        shortestWord = strs[0]
        res = ""

        for word in strs:
            if len(word) < len(shortestWord):
                shortestWord = word


        for i in range (0,len(shortestWord)):
            
            kill = 0
            
            for word in strs:
                if word[i] != shortestWord[i]:
                    kill = 1
            
            if kill == 0:
                res += shortestWord[i]
            if kill == 1:
                return res
            
        return res

          
     
mySolution = Solution()
strs = ["cir","car"]
print(mySolution.longestCommonPrefix(strs))

