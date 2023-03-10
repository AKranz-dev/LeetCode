class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        
        returnList = []
        

        for i in range(left,right+1):
            cancel = 0
            for digit in str(i):
                if digit != "0":
                    if i%int(digit) != 0:
                        cancel = 1
                else:
                    cancel = 1
            if cancel !=1 :
                returnList.append(i)   
        return returnList




s = Solution()
left = 1
right = 22
print(s.selfDividingNumbers(left,right))