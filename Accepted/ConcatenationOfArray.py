class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        counter = 0
        for i in range(2):
            counter = 0
            for item in nums:
                ans.append(nums[counter])
                counter +=1
        return ans



s = Solution()
nums = [1,2,3]
print(s.getConcatenation(nums))
