class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:

        res = 0
        temp = []

        while len(grid[0]) > 0:
            for item in grid:
                temp.append(max(item))
                item.remove(max(item))

            res += max(temp)
            temp.clear()
            
        return res



s = Solution()
grid = [[1,2,4],[3,3,1]]
print(s.deleteGreatestValue(grid))
