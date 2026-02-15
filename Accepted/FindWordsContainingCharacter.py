class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:

        # res = []
        # for word in words:
        #     if x in word:
        #         res.append(words.index(word))
        # return res

        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res


s = Solution()
words = ["leet","code"]
x = "e"
print(s.findWordsContaining(words, x))