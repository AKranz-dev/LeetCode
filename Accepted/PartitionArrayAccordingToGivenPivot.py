class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        leftList = []
        rightList = []
        midList = []
        
        for num in nums:
            if num < pivot:
                leftList.append(num)
            elif num > pivot:
                rightList.append(num)
            elif num == pivot:
                midList.append(num)
        leftList.extend(midList)
        leftList.extend(rightList)
        return leftList







s = Solution()
nums = [9,12,5,10,14,3,10] 
pivot = 10
print(s.pivotArray(nums,pivot))