class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        newList = []

        for num in nums:
            newList.append(num*num)
        
        newList = sorted(newList)
        
        return newList


nums = [-4,-1,0,3,10]
s = Solution()
print(s.sortedSquares(nums))