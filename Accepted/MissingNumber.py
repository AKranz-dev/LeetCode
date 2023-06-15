class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        return 0
            

s = Solution()
nums = [1]
print(s.missingNumber(nums))