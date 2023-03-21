class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        counter = 0
        
        for num in nums:
            for item in nums:
                if num + item == target:
                    counter +=1
        return counter
    


s = Solution()
nums = ["123","4","12","34"]
target = "1234"
print(s.numOfPairs(nums,target))