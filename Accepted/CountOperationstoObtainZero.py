class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        counter = 0
        total = 1
        
        
        while num1 !=0 and num2 !=0:
            counter +=1
            if num1 >= num2:
                num1 = (num1-num2)
            elif num2 > num1:
                num2 = (num2-num1)
        
        
        return counter






s = Solution()
num1 = 10
num2 = 10
print(s.countOperations(num1,num2))
