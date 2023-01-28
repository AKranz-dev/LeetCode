
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i=0
        lettersUsed = {}
        for letter in ransomNote:
            if letter in magazine:
                letterLimit = magazine.count(letter)
                if letter in lettersUsed.keys():
                    if lettersUsed[letter] < letterLimit:
                        lettersUsed[letter] +=1
                        i+=1
                else:
                    lettersUsed[letter] = 1
                    i+=1
            else:
                return False
        if i == len(ransomNote):
            return True
        else:
            return False
    
mySolution = Solution()

#Case 1 - expects True
ransomeNote = "a"
magazine = "a"
print(mySolution.canConstruct(ransomeNote, magazine))

#Case 2 - expects False
ransomeNote = "aa"
magazine = "ab"
print(mySolution.canConstruct(ransomeNote, magazine))

#Case 3 - expects True
ransomeNote = "aa"
magazine = "aab"
print(mySolution.canConstruct(ransomeNote, magazine))

#Case 3 - expects True
ransomeNote = "aab"
magazine = "baa"
print(mySolution.canConstruct(ransomeNote, magazine))







