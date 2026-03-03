class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:


        for x in range(k):
            sortedList = sorted(nums)
            smallest = sortedList[0]
            print(smallest)

            for y in range(0,len(nums)):
                if nums[y] == smallest:
                    nums[y] = nums[y] * multiplier
                    break
            print(nums)
        return nums


nums = [1,2]
k = 3
multiplier = 4

s = Solution()
print(s.getFinalState(nums,k,multiplier))