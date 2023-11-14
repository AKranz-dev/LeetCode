class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:

        proceed = 1
        counter = 0
        res = []
        
        while proceed == 1:
            proceed = 0
            for num in set(nums):
                if nums.count(num) >= 2:
                    nums.remove(num)
                    nums.remove(num)
                    print("Found a pair of: {}'s. Remaining nums are: {}".format(num,nums))
                    proceed = 1
                    counter +=1
            
            if proceed == 0:
                res.append(counter)
                res.append(len(nums))
                return res


            
        



s = Solution()
nums= [0]
print(s.numberOfPairs(nums))