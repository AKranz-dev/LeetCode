class Solution:
    def alternateDigitSum(self, n: int) -> int:

        digitList = []
        runningCount = 0

        for digit in str(n):
            digitList.append(digit)
    

        for i in range(1,len(digitList),2):
             digitList[i] = "-"+digitList[i]
        
        for num in digitList:
            runningCount += int(num)
        
        return runningCount


        
        
        

        

        






n = 886996
s = Solution()
print(s.alternateDigitSum(n))