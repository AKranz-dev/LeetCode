class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        res = []
        

        for letter in words[0]:
            fail = 0
            for word in words[1:]:
                if letter not in word:
                    fail = 1
            if fail == 0:
                res.append(letter)
                for i in range (len(words)-1):
                    words[i] = words[i].replace(letter,"",1)
        return res
        


s = Solution()
words = ["cool","lock","cook"]
print(s.commonChars(words))