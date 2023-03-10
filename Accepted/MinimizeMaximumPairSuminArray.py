class Solution:
    def minPairSum(self, nums: list[int]) -> int:
       
        leastList = []
        mostList = []
        valueList = []

        
        #Make a pair of the highest and lowest numbers

        nums.sort()
        #print(nums)


        for i in range(0,int(len(nums)/2)):
            #print(nums[i])
            leastList.append(nums[i])
        

        for i in range(len(nums)-1,int(len(nums)/2)-1,-1):
            #print(nums[i])
            mostList.append(nums[i])


        for least,most in zip(leastList,mostList):
            valueList.append(least+most)
        
        #print(valueList)
        return max(valueList)

        


               
        
        
        
        

nums = [3,2,4,1,1,5,1,3,5,1]
s = Solution()
print(s.minPairSum(nums))
        
        
        
        
        # - The idea is to first pair up numbers that appear twice
        # - Then, make a pair of the highest and lowest remaining number
        # - And repeat until there are no more numbers