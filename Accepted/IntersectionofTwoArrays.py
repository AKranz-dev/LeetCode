class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        res = []

        for num in set(nums1):
            if num in set(nums2) and num not in res:
                res.append(num)
        
        for num in set(nums2):
            if num in set(nums1) and num not in res:
                res.append(num)
        
        return res



s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1,nums2))