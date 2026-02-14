class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        k = 1
        while n >= 0:
            n-=k
            if n < 0:
                return k-1
            k+=1



s = Solution()
n = 1
print(s.arrangeCoins(n))