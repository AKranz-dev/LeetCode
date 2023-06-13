class Solution:
    def digitCount(self, num: str) -> bool:
        
        for i in range(len(num)):
            freq = int(num[i])

            if num.count(str(i)) != freq:
                return False
        
        return True




s = Solution()
num = "1210"
print(s.digitCount(num))