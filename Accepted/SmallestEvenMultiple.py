class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        counter = 0
        while True:
            num =  n+counter
            if num%2==0 and num%n ==0:
                return num
            else:
                counter +=1






s = Solution()
n = 5
print(s.smallestEvenMultiple(n))