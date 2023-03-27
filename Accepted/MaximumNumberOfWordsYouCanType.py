class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        wordList = []
        counter = 0
        kill = 0


        for i in range(0,len(text)):
            if text[i] != " " or i == len(text):
                wordList.append(text[i])
            
            else:
                for item in brokenLetters:
                    if item in wordList:
                        kill = 1
                
                if kill == 0:
                    counter +=1

                wordList.clear()
                kill = 0
            
            if i == len(text)-1:
                for item in brokenLetters:
                    if item in wordList:
                        kill = 1
                
                if kill == 0:
                    counter +=1

                wordList.clear()
                kill = 0

        
        return counter




s = Solution()
text = "leet code"
brokenLetters = "lt"
print(s.canBeTypedWords(text,brokenLetters))