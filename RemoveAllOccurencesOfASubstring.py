class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while part in s:
            s = s.replace(part,"")
        return s
    


a = Solution()
s = "axxxxyyyyb"
part = "xy"
print(a.removeOccurrences(s,part))