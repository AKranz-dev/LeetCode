class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:


        res = 0

        for num in nums:
            if nums.count(num) == 1:
                res +=num
        
        return res

        

s = Solution()
nums = [1,2,3,2]
print(s.sumOfUnique(nums))