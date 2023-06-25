class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        temp = sorted(nums,reverse=True)
        
        return temp[k-1]





nums = [3,2,1,5,6,4] 
k = 2
s = Solution()
print(s.findKthLargest(nums,k))
