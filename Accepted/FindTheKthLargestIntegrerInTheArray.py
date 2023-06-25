class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        tempList = []
        for item in nums:
            tempList.append(int(item))
        
        temp = sorted(tempList,reverse=True)
        
        return str(temp[k-1])





nums = ["3","6","7","10"] 
k = 4
s = Solution()
print(s.findKthLargest(nums,k))
