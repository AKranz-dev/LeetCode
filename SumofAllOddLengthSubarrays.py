class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        
        runningCount = 0
        counter = 1


        # while counter <= len(arr):
        #     for i in range (0,len(arr),counter):
        #         runningCount += arr[i]
        #     counter+=2
    

        # while counter <= len(arr):
        #     for i in range (0,len(arr),counter):
        #         for item in arr[0::counter]:
        #             print("Adding {} to {}".format(item,runningCount))
        #             runningCount += item
        #     counter+=2
        #     print(runningCount)

        
        # if len(arr)%2 == 0:
        #     maxSubArrayLength = len(arr)-1
        # else:
        #     maxSubArrayLength = len(arr)

        while counter <= len(arr):
            for item in arr[0::counter]:
                print("Adding {} to {}".format(item,runningCount))
                runningCount += item
            counter+=2
            print(runningCount)
            runningCount = 0

        





s = Solution()
arr = [1,4,2,5,3]
print(s.sumOddLengthSubarrays(arr))