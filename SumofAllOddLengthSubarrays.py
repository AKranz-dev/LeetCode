class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        
        runningCount = 0
        counter = 1


        # while counter <= len(arr):
        #     for i in range (0,len(arr),counter):
        #         runningCount += arr[i]
        #     counter+=2
    

        while counter <= len(arr):
            for i in range (0,len(arr),counter):
                for item in arr[0::counter]:
                    runningCount += item
            counter+=2
            print(runningCount)


        

        




s = Solution()
arr = [1,4,2,5,3]
print(s.sumOddLengthSubarrays(arr))