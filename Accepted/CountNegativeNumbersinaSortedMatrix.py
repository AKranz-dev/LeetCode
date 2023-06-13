class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:

        counter = 0


        for group in grid:
            if min(group) > -1:
                continue
            else:
                for num in group:
                    if num < 0:
                        counter+=1
        return counter
    

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
s = Solution()
print(s.countNegatives(grid))