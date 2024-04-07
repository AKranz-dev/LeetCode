class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:

        res = []

        for num in nums:
            for char in str(num):
                res.append(int(char))
        return res



        
nums = [13,25,83,77]
a = Solution()
print(a.separateDigits(nums))