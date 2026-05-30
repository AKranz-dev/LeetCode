class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:

        res = []

        for i,mountain in enumerate(height):
            if i == 0:
                lastHeight = mountain
                continue

            if lastHeight > threshold:
                res.append(i)
                lastHeight = mountain
            
            else:
                lastHeight = mountain
                continue
 
        
        return res







height = [1,2,3,4,5]
threshold = 2
s = Solution()
print(s.stableMountains(height,threshold))