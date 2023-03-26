class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        sList = []
        counter = 0

        for letter in s:
            if letter not in sList:
                sc = s.count(letter)
                tc = t.count(letter)
                if sc != tc and letter not in sList:
                        sList.append(letter)
                        counter += abs(sc-tc)
                elif sc == tc:
                    sList.append(letter)
    
        
        for letter in t:
            if letter not in sList:
                sc = s.count(letter)
                tc = t.count(letter)
                if sc != tc and letter not in sList:
                    sList.append(letter)
                    counter += abs(sc-tc)

        return counter



s = "leetcode"
t = "coats"
p = Solution()
print(p.minSteps(s,t))