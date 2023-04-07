class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:

        while True:
            if original not in nums:
                return original
            original *=2



s = Solution()
nums = [5,3,6,1,12]
original = 3

print(s.findFinalValue(nums,original))