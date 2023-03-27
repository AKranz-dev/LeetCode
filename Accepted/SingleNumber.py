class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num

s = Solution()
nums = [1,2,2,3,3]
print(s.singleNumber(nums))