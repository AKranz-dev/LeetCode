class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:

        counter = len(words)

        for word in words:
            if len(pref) > len(word):
                counter-=1
                continue
            if pref != word[:len(pref)]:
                counter-=1
        
        return counter


        

pref = "at"
words = ["pay","attention","practice","attend"]
s = Solution()
print(s.prefixCount(words,pref))