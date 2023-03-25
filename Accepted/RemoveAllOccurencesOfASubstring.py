class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while part in s:
            s = s.replace(part,"",1)
        return s
    


a = Solution()
s = "aabababa"
part = "aba"
print(a.removeOccurrences(s,part))