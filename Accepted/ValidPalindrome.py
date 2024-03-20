class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = s.lower()
        s = s.replace(" ","")

        for letter in set(s):
            if letter.isalnum():
                W=1
            else:
                s = s.replace(letter,"")
        
        for letter,char in zip(s[0:],s[::-1]):
            if letter !=char:
                return False
        return True
            




s = "A man, a plan, a canal: Panama"
a = Solution()
print(a.isPalindrome(s))