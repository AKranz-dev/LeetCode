class Solution:
    def countDigits(self, num: int) -> int:
        digitList = []
        counter = 0
        for digit in str(num):
            digitList.append(digit)
        
        for digit in digitList:
            if num%int(digit) ==0:
                counter +=1
        return counter


s = Solution()
num = 7
print(s.countDigits(num))