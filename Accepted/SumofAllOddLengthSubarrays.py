class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        
        subLens = []
        addList = []
        res = 0

        for i in range(len(arr)+1):
            if i%2 != 0:
                subLens.append(i)
          
        for item in subLens:
            hold = item
            start = 0   
            
            for num in arr:
                addList.append(arr[start:item])
                start+=1
                item +=1
                
                if item-1+start-1-len(arr) == len(arr)-hold:
                    break

        for list in addList:
            for item in list:
                res += item
        
        return res
             

s = Solution()
arr = [1,4,2,5,3]
print(s.sumOddLengthSubarrays(arr))