class Solution:
    def trailingZeroes(self, n: int) -> int:

        res = n
        counter = 0

        if n <= 4:
            return 0
        else:
         for i in range(n-1,0,-1):
            res *= i
        

        strres = str(res)
        
        for x in range (len(strres),0,-1):
           if strres[x-1] == '0':
              counter +=1
           else:
              return counter
           

        


    
n = 7
s = Solution()
print(s.trailingZeroes(n))