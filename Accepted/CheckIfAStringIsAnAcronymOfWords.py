class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:



        # res = ""
        # for word in words:
        #     res+=word[0]
        # if res == s:
        #     return True
        # else:
        #     return False
        

        for word,letter in zip(words,s):
            if word[0] != letter:
                return False   
        return True





a = Solution()
words = ["alice","bob","charlie"]
s = "abc"
print(a.isAcronym(words,s))