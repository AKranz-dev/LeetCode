#https://leetcode.com/problems/valid-parentheses/discussion/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []


        if len(s)%2 !=0:
            return False


        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            
            elif len(stack) == 0:
                return False
            
            elif char == ")":
                if stack[len(stack)-1] != "(" or len(stack) == 0:
                    return False
                else:
                    stack.pop(len(stack)-1)

            elif char == "]":
                if stack[len(stack)-1] != "[" or len(stack) == 0:
                    return False
                else:
                    stack.pop(len(stack)-1)

            elif char == "}":
                if stack[len(stack)-1] != "{" or len(stack) == 0:
                    return False
                else:
                    stack.pop(len(stack)-1)
                    
        
        if len(stack) > 0:
            return False
        return True


a = Solution()
s = "){"
print(a.isValid(s))