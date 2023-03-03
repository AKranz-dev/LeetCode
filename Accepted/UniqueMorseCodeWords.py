class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        dict = {}
        wordList = []
        storageList = []
        
        for letter,symbol in zip(alphabet,morseList):
            dict[letter] = symbol



        for word in words:
            wordList.clear()
            for letter in word:
                wordList.append(dict[letter])
                morseSymbol = "".join(wordList)
            if morseSymbol not in storageList:
                storageList.append(morseSymbol)
        return len(storageList)

            






s = Solution()
words = ["gin","zen","gig","msg"]
print(s.uniqueMorseRepresentations(words))