class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        top = "qwertyuiop"
        middle = "asdfghjkl"
        bottom = "zxcvbnm"
        res = []

        for word in words:
            
            stop = 0
            
            if word[0].lower() in top:
                for letter in word:
                    if letter.lower() not in top:
                        stop = 1
                if stop == 0:
                    res.append(word)
                else:
                    print("{} was not in {}".format(word,top))
            
            elif word[0].lower() in middle:
                for letter in word:
                    if letter.lower() not in middle:
                        stop = 1
                if stop == 0:
                    res.append(word)
                else:
                    print("{} was not in {}".format(word,middle))
            
            
            elif word[0].lower() in bottom:
                for letter in word:
                    if letter.lower() not in bottom:
                        stop = 1
                if stop == 0:
                    res.append(word)
                else:
                    print("{} was not in {}".format(word,bottom))
        
        return res

s = Solution()
words = ["a","b"]
print(s.findWords(words))
