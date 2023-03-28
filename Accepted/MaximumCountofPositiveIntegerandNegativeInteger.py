class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        
        posList = []
        negList = []

        for num in nums:
            if num > 0:
                posList.append(num)
            elif num < 0:
                negList.append(num)
        
        return max(len(posList),len(negList))



nums = [-2,-1,-1,1,2,3]
s = Solution()
print(s.maximumCount(nums))