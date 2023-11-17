class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:

        res = 0
        for i in range(k):
            target = max(nums)
            res+=target
            nums.remove(target)
            nums.append(target+1)
        return res
        


s = Solution()
nums = [1,2,3,4,5]
k = 3
print(s.maximizeSum(nums,k))