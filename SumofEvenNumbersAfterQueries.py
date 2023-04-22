class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        

        #Both solutions are working, but both are only fast enough to pass 53/58 test cases
        
        # res = []
        
        # for item in queries:
        #     runningCount = 0
        #     nums[item[1]] += item[0]
            
            
            
        #     for item in nums:
        #         if item%2 == 0:

        #             runningCount += item
            
            
        #     res.append(runningCount)
        
        
        # return res


        #====================================================================================================


        #0 means that the number is odd
        #1 means that the number is even
        #2 means that the number needs to be checked

        res = []
        knownEven = {}

        for i in range (len(nums)):
            if nums[i]%2 == 0:
                knownEven[i] = 1
            else:
                knownEven[i] = 0
        
        for item in queries:
            # print(nums)
            # print(knownEven)
            runningCount = 0

            nums[item[1]] += item[0]
            
            if nums[item[1]]%2 == 0:
                knownEven[item[1]] = 1
            else:
                knownEven[item[1]] = 0

            
            for item in knownEven:
                if knownEven[item] == 1:
                    runningCount+=nums[item]
            
            res.append(runningCount)
        
        
        return res


s = Solution()

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(s.sumEvenAfterQueries(nums,queries))