class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:

        res = []

        for num in nums:
            if num % 2 == 0:
                res.append(0)
            else:
                res.append(1)

        return sorted(res)

s = Solution()
nums = [4,3,2,1]
print(s.transformArray(nums))