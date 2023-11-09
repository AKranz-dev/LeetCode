class Solution:
    def arraySign(self, nums: list[int]) -> int:

        res = 1
        if 0 in nums:
            return 0
       
        for num in nums:
            res = res*num
        
        if res<0:
            return -1
        else:
            return 1


s = Solution()
nums = [-1,-2,-3,-4,3,2,1]
print(s.arraySign(nums))