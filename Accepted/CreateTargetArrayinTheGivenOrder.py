class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:

        res = []

        for num,item in zip(nums,index):
            res.insert(item,num)
        return res





nums = [0,1,2,3,4]
index = [0,1,2,2,1]
s = Solution()
print(s.createTargetArray(nums,index))