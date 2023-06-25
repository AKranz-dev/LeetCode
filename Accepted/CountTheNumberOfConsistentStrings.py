class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:

        counter = 0

        for word in words:
            kill = 0
            for letter in set(word):
                if letter not in allowed:
                    kill = 1
            if kill == 0:
                counter +=1
        return counter

    
s = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(s.countConsistentStrings(allowed,words))