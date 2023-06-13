import math
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:


        temp = []
        res = []
        start = 0


        #This is the remainder - AKA the number of fill characters we will need - could be 0 or could be >0.
        remainingChars = len(s)%k
        fillCount = k - remainingChars
        
        print(remainingChars)
        print(fillCount)


        #The number of times we are garunteed to make groups without filling
        iterations = (len(s)/k)
        iterations = math.floor(iterations)


        #Catches if we cannot make any groups, and jump immedietly to filling
        if iterations == 0:
            tempString = s+(fill*fillCount)
            res.append(tempString)
            return res


        #Fills in all the perfect groups possible
        for i in range(iterations):
            res.append(s[start:start+k])
            start = start+k
        print(res)

        
        #Checks if we have any remaining characters.
        if remainingChars !=0:

            #Take care of the remaining chars in s, and provide fills.
            tempString = s[len(s)-1:len(s)-1-remainingChars:-1]
            temp.append(tempString[::-1])

            
            for i in range(fillCount):
                temp.append(fill)

            remainder = "".join(temp)
            res.append(remainder)
        
        return res
        
                


a = Solution()
s = "bgycymgbblobvpdf"
k = 67
fill = "u"
print(a.divideString(s,k,fill))
#["bgycymgbblobvpdfuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"]


