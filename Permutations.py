class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        numList = []
        returnList = []
        
        for i in range(0,len(nums)-1):
            numList.append(nums)






nums = [1,2,3]
s = Solution()
print(s.permute(nums))