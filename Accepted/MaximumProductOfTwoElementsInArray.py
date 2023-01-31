class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        lastNum = nums[(len(nums))-1]
        slastNum = nums[(len(nums))-2]
        result = (lastNum-1)*(slastNum-1)
        return result
        


s = Solution()
nums = [3,4,5,2]
print(s.maxProduct(nums))