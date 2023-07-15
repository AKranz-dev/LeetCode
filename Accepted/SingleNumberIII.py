class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:


        res = []
        for item in set(nums):
            if nums.count(item) == 1:
                res.append(item)
        return res


nums = [1,2,1,3,2,5]
s = Solution()
print(s.singleNumber(nums))