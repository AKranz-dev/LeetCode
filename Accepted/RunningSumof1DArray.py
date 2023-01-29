class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningCount = 0
        countList = []
        for num in nums:
            runningCount += num
            countList.append(runningCount)

        return countList

        


s = Solution()
nums = [1,2,3,4]
print(s.runningSum(nums))