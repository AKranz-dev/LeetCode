class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        letterList = []
        spaceCounter = 0
        returnList = []

        
        
        for letter in s:
            if spaceCounter>=k:
                break
            if letter !=" ":
                letterList.append(letter)
            else:
                returnWord = "".join(letterList)
                returnList.append(returnWord)
                returnWord = ""
                letterList.clear()
                spaceCounter = spaceCounter+1
        
        if k > spaceCounter:
            return s
        return " ".join(returnList)


a = Solution()
s = "Hello how are you Contestant"
k = 4
print(a.truncateSentence(s,k))