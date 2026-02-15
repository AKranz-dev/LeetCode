class Solution:
    def scoreOfString(self, word: str) -> int:


        res = 0
        for x in range(len(word)):
            if x != (len(word)-1):
                res+=abs((ord(word[x]))-(ord(word[x+1])))
            else:
                return res




word = "hello"
s = Solution()
print(s.scoreOfString(word))