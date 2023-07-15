import math
class Solution:
    def integerReplacement(self, n: int) -> int:

        counter = 0
        
        while n > 1:

            if n%2 == 0:
                n = math.floor(n/2)
                counter +=1
            
            elif (math.floor((n-1)/2))%2 == 0 or n-1==2:
                n -= 1
                counter +=1
            
            elif (math.floor((n+1)/2))%2 == 0 or n+1==4:
                n+=1
                counter +=1
        
        return counter

s = Solution()
n = 65535
print(s.integerReplacement(n))