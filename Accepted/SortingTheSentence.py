class Solution:
    def sortSentence(self, s: str) -> str:
        
        letterList = []
        wordDict = {}
        returnWord = []

        
        for letter in s:
            if letter.isalpha():
                letterList.append(letter)
            elif letter.isnumeric():
                wordDict[letter] = "".join(letterList)
                letterList.clear()
        
        myKeys = list(wordDict.keys())
        myKeys.sort()
        sortedDict = {i: wordDict[i] for i in myKeys}

        for item in sortedDict.values():
            returnWord.append(item)
        return " ".join(returnWord)
        







a = Solution()
s = "is2 sentence4 This1 a3"
print(a.sortSentence(s))