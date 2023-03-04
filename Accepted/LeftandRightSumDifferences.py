class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:

        leftList = []
        rightList = []
        returnList = []


        for i in range(0,len(nums)):
            runningLeft = 0
            for x in range(0,i):
                runningLeft += nums[x]
            leftList.append(runningLeft)
        


        for i in range(0,len(nums)):
            runningRight = 0
            for x in range(i+1,len(nums)):
                runningRight += nums[x]
            rightList.append(runningRight)


        
        for num,item in zip(leftList,rightList):
             returnList.append(abs(num-item))
        return returnList


        
        
        
        
        




s = Solution()
nums = [10,4,8,3]
print(s.leftRigthDifference(nums))