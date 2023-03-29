class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:

        numSet = set()
        returnList = []
        counter = 0

        #Get all unique numbers from all arrays
        for num in nums1:
            numSet.add(num)
        for num in nums2:
            numSet.add(num)
        for num in nums3:
            numSet.add(num)
        
        for num in numSet:
            if num in nums1:
                counter += 1
            if num in nums2:
                counter += 1
            if num in nums3:
                counter += 1
            if counter >1:
                returnList.append(num)
            counter = 0
        return returnList
            
            

            





a = Solution()
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(a.twoOutOfThree(nums1,nums2,nums3))