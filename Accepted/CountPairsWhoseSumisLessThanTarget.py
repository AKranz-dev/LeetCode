class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:


        counter = 0

        for num in range(len(nums)):  #tracks the index of the first iteration (-1,1,2,3,1)
            for sub in range(num+1,len(nums)):  #tracks the index of the second number of the pair (-1,1), (-1,2), (-1,3)

                if num < sub and nums[num] + nums[sub] < target:
                    #print("({},{})".format(num,sub))
                    counter +=1
        return counter

            


s = Solution()
nums = [-1,1,2,3,1]
target = 2
print( s.countPairs(nums,target))