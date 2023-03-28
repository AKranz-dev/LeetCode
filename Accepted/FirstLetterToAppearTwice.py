class Solution:
    def repeatedCharacter(self, s: str) -> str:


        dict = {}
        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                return letter

a = Solution()
s = "abccbaacz"
print(a.repeatedCharacter(s))