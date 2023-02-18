class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            if num%2 == 0:
                num = num/2
                counter +=1
            else:
                num -= 1
                counter +=1
        return counter
        


s = Solution()
num = 14
print(s.numberOfSteps(num))