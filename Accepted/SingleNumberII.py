class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for item in set(nums):
            if nums.count(item) == 1:
                return item

nums = [2,2,3,2]
s = Solution()
print(s.singleNumber(nums))