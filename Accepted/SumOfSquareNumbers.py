import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c ==0:
            return True
        
        sqrt = math.sqrt(c)
        
        for i in range(1,math.floor(sqrt)+1):
            remainder = c-(i*i)
            
            if math.sqrt(remainder) % 1 == 0:
                return True
        return False
            

s = Solution()
c = 5
print(s.judgeSquareSum(c))