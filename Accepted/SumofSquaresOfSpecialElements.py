class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:

        specialList = []
        res = 0

        for i in range(1,len(nums)+1):
            if len(nums) % i == 0:
                specialList.append(nums[i-1])

        for num in specialList:
            res += (num*num)
        
        return res



s = Solution()
nums = [2,7,1,19,18,3]
print(s.sumOfSquares(nums))