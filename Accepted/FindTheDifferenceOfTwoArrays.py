class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        listOne = []
        listTwo = []
        returnList = []
        
        for num in nums1:
            if num not in nums2 and num not in listOne:
                listOne.append(num)
        for num in nums2:
            if num not in nums1 and num not in listTwo:
                listTwo.append(num)
        
        
        returnList.append(listOne)
        returnList.append(listTwo)
        
        return returnList





s = Solution()
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(s.findDifference(nums1,nums2))