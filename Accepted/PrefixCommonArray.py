class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:


        res = []
        #Iterate through A
        for x in range(len(A)):
            
            value = 0
            #For all characters from the beginning to the current index
            for y in range(0,x+1):
                #If the character is also in list B, we add +1
                if A[y] in B[0:x+1]:
                    value+=1
            
            res.append(value)
        return res



s = Solution()
A = [1,3,2,4]
B = [3,1,2,4]
print(s.findThePrefixCommonArray(A,B))