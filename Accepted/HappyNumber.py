class Solution:
    def isHappy(self, n: int) -> bool:

        total = 0
        counter = 0

        while counter < 100:
            total = 0
            print("Number to check: {}".format(n))
            for i in range(len(str(n))):
                
                print("Checking {}'th digit, which is {}".format(i,str(n)[i]))

                total += (int(str(n)[i]) * int(str(n)[i]))
            
            
            n = total
            counter +=1
            if n == 1:
                return True
        
        return False

n = 2
s = Solution()
print(s.isHappy(n))