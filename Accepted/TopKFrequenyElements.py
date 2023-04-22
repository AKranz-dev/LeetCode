class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        countDict = {}
        res = []

        for num in set(nums):
            countDict[num] = nums.count(num)
        
        countDict = dict(sorted(countDict.items(), key=lambda item: item[1],reverse=True))
        
        res.extend(countDict.keys())
        return res[0:k]



s = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
print(s.topKFrequent(nums,k))