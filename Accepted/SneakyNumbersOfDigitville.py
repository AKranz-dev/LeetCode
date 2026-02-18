class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        res = []
        
        while len(res) < 2:
            for num in set(nums):
                if nums.count(num) > 1:
                    res.append(num)
        return res

s = Solution()
nums = [0,1,1,0]
print(s.getSneakyNumbers(nums))