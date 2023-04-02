class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:

        costs.sort()
        barCount = 0

        for bar in costs:
            if coins - bar < 0:
                return barCount
            coins -=bar
            barCount +=1
        
        return barCount



s = Solution()
costs = [1,3,2,4,1]
coins = 7
print(s.maxIceCream(costs,coins))
