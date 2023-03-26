class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:

        maxList = []
        returnList = []
        counter = 0
        x=0

        arr.sort()

        for i in range(len(arr)-1,0,-1):
                if arr[i] not in maxList and x<k:
                    maxList.append(arr[i])
                    x+=1
        
        for item in maxList:
            while len(returnList) < len(arr) and returnList.count(item) < k:
                returnList.append(item)
        
        
        for item in returnList:
            counter +=item
        

        print(arr)
        print(maxList)
        print(returnList)


        return counter




s = Solution()
arr = [1,4,1,5,7,3,6,1,9,9,3]
k = 4
print(s.maxSumAfterPartitioning(arr,k))