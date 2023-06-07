class Solution:
    def smallestEqual(self, nums: list[int]) -> int:

        error = 0 
        lowestIndex = []

        
        for i in range(len(nums)):
            if i%10 == nums[i]:
                lowestIndex.append(i)
            else:
                error += 1
 
        
        if error == len(nums):
            return -1
        else:
            return min(lowestIndex)
        




s = Solution()
nums = [0,1,2]
print(s.smallestEqual(nums))