class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        letterList = []
        for letter in sentence:
            letterList.append(letter)
        letterSet = set(letterList)
        
        if len(letterSet) != 26:
            return False
        else:
            return True





s = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(sentence))