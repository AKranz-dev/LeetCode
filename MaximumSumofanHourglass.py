class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:

        #I misunderstood the question... will need a different approach
        runCount = 0

        for item in grid[0]:
            runCount +=item
            print("Adding {} from the first set".format(item))
        
        skippedItems = len(grid[0]) // 2
        skippedItems = skippedItems // 2

        for i in range(1,len(grid)-1):

            for x in range(len(grid[0]) // 2):
                runCount += grid[i][skippedItems+x]
                print("Adding {} to the body from set {}".format(grid[i][skippedItems+x],grid[i]))
        
        for item in grid[len(grid)-1]:
            runCount +=item
            print("Adding {} from the last set".format(item))
        
        return runCount


s = Solution()
grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
print(s.maxSum(grid))