class Solution:
    def maxDistinct(self, s: str) -> int:

        return(len(set(s)))
        
l = Solution()
s = "abab"
print(l.maxDistinct(s))