import math
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        
        #Defines the amount of candies Alice can eat
        target = math.floor(len(candyType)/2)
        
        #Stores number of unique candies available
        uniqueCandies = len(set(candyType))

        if target < uniqueCandies:
            return target
        elif target > uniqueCandies:
            return uniqueCandies
        elif target == uniqueCandies:
            return target

        


candyType = [1,1,2,2,3,3]
s = Solution()
print(s.distributeCandies(candyType))