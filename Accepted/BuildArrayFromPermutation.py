class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:

        res = []

        for i in range (len(nums)):
            res.append(nums[nums[i]])
        return res


s = Solution()
nums = [0,2,1,5,3,4]
print(s.buildArray(nums))