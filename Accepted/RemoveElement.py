class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # returnList = []
        # matchDict = {}
        # dictCounter = 1
        # k=0

        # for num in nums:
        #     if num == val:
        #         k+=1
        #         matchDict[nums.index(num)] = 1 #Matched the target value, take note of it's index location in the list and use that as a key. It's value is 1, meaning it needs to be replaced
        #     else:
        #         #First, check if there are any values in the list that need to be replaced
        #         if 1 in matchDict.values():   #If there is anything marked for replacement in the dictionary
        #             for item in matchDict:
        #                 if matchDict[item] == 1:
        #                     nums[item] = num #Replace the value in nums (at the index location that is marked for replacement) with the nums value that is passable
        #         else: #If there are no values marked for replacement, you can staty where you are (i.e. do nothing)
        #             i=0
        
        # print(nums)
        # return k

        numList = []
        for num in nums:
            if num != val:
                numList.append(num)
        
        remainderCount = len(numList)

        while len(numList) != len(nums):
            numList.append("X")
        
        nums.clear()
        for num in numList:
            nums.append(num)
        
        return remainderCount







mySolution = Solution()
nums = [3,2,2,3]
val = 3
print(mySolution.removeElement(nums,val))
