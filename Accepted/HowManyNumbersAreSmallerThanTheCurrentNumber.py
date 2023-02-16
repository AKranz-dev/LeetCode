class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        counter = 0
        countList = []
        for num in nums:
            counter = 0
            for item in nums:
                if item<num:
                    counter+=1
            countList.append(counter)
        return countList


s = Solution()
nums = [8,1,2,2,3]
print(s.smallerNumbersThanCurrent(nums))