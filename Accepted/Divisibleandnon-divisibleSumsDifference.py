class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        res1 =[]
        res2 =[]

        for num in range(1,n+1):
            if num % m != 0:
                res1.append(num)
            else:
                res2.append(num)
        return(sum(res1)-sum(res2))




s = Solution()
n = 10
m = 3
print(s.differenceOfSums(n,m))