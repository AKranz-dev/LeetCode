class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        import math
        freq = s.count(letter)
        return math.floor((freq/len(s)*100))
    

a = Solution()
s = "foobar"
letter = "o"
print(a.percentageLetter(s,letter))