class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        returnList = []

        #base case
        if n in nums and k ==1:
            returnList.append(n)
            return returnList


            

                    



s = Solution()
k = 3
n = 7
print(s.combinationSum3(k,n))



#First, subtract a number from our target. 
# Then, check if the remainder can be broken into (k-1) numbers