class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        numsLength = len(nums)
        counter = 0
        for number in nums:
            checksRemaining = (numsLength-1)-nums.index(number)
            checkIndex=1
            for step in range(0,checksRemaining):
                currentNumberIndex = nums.index(number) #Does not account for duplicate numbers - it will choose the index of the first number it sees.
                if number == nums[currentNumberIndex + checkIndex]:
                    counter +=1
                checkIndex +=1
        return int(counter/2) #Which is why we have to divide by 2 at the end

s = Solution()
nums = [1,2,3,1,1,3]
print(s.numIdenticalPairs(nums))