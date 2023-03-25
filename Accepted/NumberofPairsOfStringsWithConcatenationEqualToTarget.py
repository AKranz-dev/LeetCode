class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        counter = 0
    
        for i in range(0,len(nums)):
            for x in range(0,len(nums)):
                if nums[i] + nums[x] == target and i != x:
                    counter +=1
        return counter

    


s = Solution()
nums = ["777","7","77","77"]
target = "7777"
print(s.numOfPairs(nums,target))