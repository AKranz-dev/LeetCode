class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:


        counter = 1
        max = 0

        for x in range(len(nums)):
            if x != (len(nums)-1) and nums[x+1] > nums[x]:
                counter +=1
            else:
                if counter >= (len(nums)/2):
                    return counter
                if counter > max:
                    max = counter
                counter = 1
        return max






a = Solution()
nums = [1,3,5,4,7]
print(a.findLengthOfLCIS(nums))