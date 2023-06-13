class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        result = []
        start = 0
        nums = sorted(nums)

        while True:
            try:
                index = nums.index(target,start)
                result.append(index)
                start = index+1
            except:
                return result



s = Solution()
nums = [1,2,5,2,3]
target = 3
print(s.targetIndices(nums,target))
