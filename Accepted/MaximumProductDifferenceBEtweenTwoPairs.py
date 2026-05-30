class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:

        sortedNums = sorted(nums)
        return (sortedNums[len(nums)-1] * sortedNums[len(nums)-2]) - (sortedNums[1] * sortedNums[0])
        





nums = [5,6,2,7,4]
s = Solution()
print(s.maxProductDifference(nums))