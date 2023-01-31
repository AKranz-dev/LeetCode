class Solution:
    def pivotInteger(self, n: int) -> int:
        runningCount = 0 #The sum of all numbers up to and including the current number
        afterCount = 0
        if n == 1 :
            return 1
        for i in range(1,n): #For every number, check if the running count up to that number is equal to the sum of that number and all others after it.
            runningCount += i
            print("Running count is {}".format(runningCount))
            afterCount = 0
            for num in range(i,n+1):
                afterCount += num
                print("Aftercount is {}".format(afterCount))
            if runningCount == afterCount:
                return i
        if runningCount != afterCount:
            return -1






s = Solution()
n = 8
print(s.pivotInteger(n))