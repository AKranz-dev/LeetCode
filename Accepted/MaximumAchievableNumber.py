class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:

        return num+(2*t)


s = Solution()
num = 4
t = 1
print(s.theMaximumAchievableX(num,t))