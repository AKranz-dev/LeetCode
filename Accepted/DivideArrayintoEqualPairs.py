class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        if len(nums)%2 !=0:
            return False
        

        div = len(nums)/2

        for num in nums:
            if nums.count(num)%2 !=0:
                return False
        return True



s = Solution()
nums = [3,2,3,2,2,2]
print(s.divideArray(nums))