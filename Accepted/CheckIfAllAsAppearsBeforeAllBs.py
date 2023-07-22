class Solution:
    def checkString(self, s: str) -> bool:

              
        #Base cases
        if 'a' not in s or 'b' not in s:
            return True

        #Reversing the string
        srev = s[::-1]
        
        #Make sure there are no B's after this value
        aind = srev.index('a')
        
        #Grab a slice of the string to check for B's
        testSlice = srev[aind:]

        if 'b' in testSlice:
            return False
        else:
            return True

        # if bind < aind:
        #     return True
        # elif aind > bind:
        #     return False
        


s = "abab"
a = Solution()
print(a.checkString(s))

#baba