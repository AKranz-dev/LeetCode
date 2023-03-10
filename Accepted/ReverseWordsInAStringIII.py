class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = []
        finalList = []

        for i in range(0,len(s)):
            if s[i] == " ":
                wordList.reverse()
                returnString = "".join(wordList)
                finalList.append(returnString)
                wordList.clear()
            elif i == len(s)-1:
                wordList.append(s[i])
                wordList.reverse()
                returnString = "".join(wordList)
                finalList.append(returnString)
            else:
                wordList.append(s[i])
        return " ".join(finalList)
    




zz = Solution()
s = "Let's take LeetCode contest"
print(zz.reverseWords(s))