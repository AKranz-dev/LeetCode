class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        numsLength = len(nums)
        counter = 0
        for number in nums:
            checksRemaining = (numsLength-1)-nums.index(number)
            checkIndex=1
            for step in range(0,checksRemaining):
                currentNumberIndex = nums.index(number)
                if number == nums[currentNumberIndex + checkIndex]:
                    counter +=1
                checkIndex +=1
        return int(counter/2)

s = Solution()
nums = [1,2,3,1,1,3]
print(s.numIdenticalPairs(nums))