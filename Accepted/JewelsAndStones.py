class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelCounter = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    jewelCounter +=1
        return jewelCounter