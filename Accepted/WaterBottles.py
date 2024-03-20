import math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        drankCount = numBottles

        print(math.floor(15/4))

        while numBottles >= numExchange:
            leftOverBottles = numBottles % numExchange
            drankCount += math.floor(numBottles/numExchange)
            numBottles = leftOverBottles + math.floor(numBottles/numExchange)
        
        return drankCount
        
            




        
a = Solution()
numBottles = 15
numExchange = 4
print(a.numWaterBottles(numBottles, numExchange))