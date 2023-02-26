class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        counter = 0
        for num in nums:
            for item in nums:
                if abs(num-item) == k:
                    counter += 1
        return int(counter/2)




s = Solution()
nums = [1,2,2,1]
k = 1
print(s.countKDifference(nums,k))