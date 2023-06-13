class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        original = len(nums)
        numSet = set(nums)
        new = len(numSet)

        if original != new:
            return True
        else:
            return False

s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums))