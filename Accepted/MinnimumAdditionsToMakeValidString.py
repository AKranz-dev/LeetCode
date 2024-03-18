class Solution:
    def addMinimum(self, word: str) -> int:
        
        orig = len(word)
        count = 0
        lettersRemoved = 0
    
        L = word.count("abc")
        x = word.count("ab") - L
        z = word.count("bc") - L
        y = word.count("ac")

        if L > 0:
            word = word.replace("abc","")
            lettersRemoved += (L*3)

        if x > 0:
            word = word.replace("ab","")
            count += x
            lettersRemoved += (x*2)

        if y > 0:
            word = word.replace("ac","")
            count += y
            lettersRemoved += (y*2)
        
        if z > 0:
            word = word.replace("bc","")
            count += z
            lettersRemoved += (z*2)


        diff = (orig-lettersRemoved)
        return count + (diff*2)
        
        

a = Solution()
word = "baccbc"
print(a.addMinimum(word))
