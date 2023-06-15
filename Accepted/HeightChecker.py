class Solution:
    def heightChecker(self, heights: list[int]) -> int:

        heightsSorted = sorted(heights)

        counter = 0

        for entry,num in zip(heights,heightsSorted):
            if entry != num:
                counter +=1
        return counter

s = Solution()

heights = [1,1,4,2,1,3]
print(s.heightChecker(heights))