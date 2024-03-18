class Solution:
    def isPalindrome(self, x: int) -> bool:


        x = str(x)

        for char,item in zip(x[0:], x[::-1]):
            # print(char)
            # print("Left character is {}, right character is {}".format(char,item))
            if char != item:
                return False
        return True



a = Solution()
x = 121
print(a.isPalindrome(x))