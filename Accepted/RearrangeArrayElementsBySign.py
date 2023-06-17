class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:


        posSet = []
        negSet = []
        res = []

        for num in nums:
            if num < 0:
                negSet.append(num)
            else:
                posSet.append(num)
        
        print(negSet)
        print(posSet)


        for num,item in zip(posSet,negSet):
            res.append(num)
            res.append(item)
        
        print(res)
        return res








nums = [3,1,-2,-5,2,-4]
s = Solution()
print(s.rearrangeArray(nums))