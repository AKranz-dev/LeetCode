class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        returnList = []

        for kid in candies:
            currentKid = kid + extraCandies
            if currentKid >= maxCandies:
                returnList.append(True)
            else:
                returnList.append(False)
        return returnList




s = Solution()
candies =[2,3,5,1,3]
extraCandies = 3
print(s.kidsWithCandies(candies,extraCandies))
