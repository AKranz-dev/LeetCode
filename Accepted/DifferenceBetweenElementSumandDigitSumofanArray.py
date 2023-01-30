class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
       
        #Calculate The element sum of nums (running count)
        runningCount = 0
        for num in nums: 
            runningCount += num
        

        #Calculate The digit sum of nums (running count)
        digitrunningCount = 0
        for num in nums:
                for digit in str(num):
                    digitrunningCount += int(digit)
        
        #Add both together and return

        result = runningCount - digitrunningCount
        return result

            



s = Solution()
nums = [1,15,6,3]
print(s.differenceOfSum(nums))