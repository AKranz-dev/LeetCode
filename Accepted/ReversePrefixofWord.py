class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        tempList = []

        if ch not in word:
            return word

        
        for i in range(len(word)):
            if word[i] == ch:
                tempList.append(word[i])
                index = i
                break
            else:
                tempList.append(word[i])
        
        tempList.reverse()
        res = "".join(tempList)
        
        for i in range(i+1,len(word)):
            res+=word[i]
        
        return res




s = Solution()
word = "abcd"
ch = "z"
print(s.reversePrefix(word,ch))