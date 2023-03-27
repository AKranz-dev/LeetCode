class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:

        oddList = []
        evenList = []
        returnList = []

        for num in nums:
            if num%2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
        
        for i in range(0,int(len(nums)/2)):
            returnList.append(evenList[i])
            returnList.append(oddList[i])
        
        return returnList


s = Solution()
nums = [4,2,5,7]
print(s.sortArrayByParityII(nums))