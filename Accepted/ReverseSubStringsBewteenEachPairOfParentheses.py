class Solution:
    def reverseParentheses(self, s: str) -> str:

        openParenLocations = []
        closedParenLocations = []

        while "(" in s:
            
            openParenLocations.clear()
            closedParenLocations.clear()

            for i in range(len(s)):
                if s[i] == "(":
                    l = i
                elif s[i] == ")":
                    r = i
                    break


            subString = s[l+1:r]
            revSubString = subString[::-1]
                
            s = s[:l] + revSubString + s[r+1:]   
        return s





s = "(ed(et(oc))el)"
a = Solution()
print(a.reverseParentheses(s))

#(ed(etco)el)
#(edocteel)