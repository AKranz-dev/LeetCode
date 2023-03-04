class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        dict = {}
        returnList = []

        for name,height in zip(names,heights):
            dict[height] = name
        
        heights.sort(reverse=True)
        

        for height in heights:
            returnList.append(dict[height])
        return returnList






s = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(s.sortPeople(names,heights))