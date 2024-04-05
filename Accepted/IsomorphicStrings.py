class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        letterDict = {}

        for letter, item in zip(s,t):

            if letter not in letterDict and item not in letterDict.values():
                letterDict[letter] = item
            elif letter in letterDict and item == letterDict[letter]:
                continue
            else:
                return False
        return True


a = Solution()
s = "egg"
t = "add"
print(a.isIsomorphic(s,t))