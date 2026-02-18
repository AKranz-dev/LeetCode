class Solution:
    def alternatingSum(self, nums: list[int]) -> int:

        res = nums[0]
        operation = "-"
        
        for num in nums[1:]:
            if operation == "-":
                res -=num
                operation = "+"
            else:
                res +=num
                operation = "-"
        return res



s = Solution()
nums = [1,3,5,7]
print(s.alternatingSum(nums))