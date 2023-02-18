class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        keyDict = {}
        indexCount = 0
        decodeList = []

        for letter in key: #Key to value - meaning the key letter is the dict key and the dict value is the corresponding alphabet letter
            if letter.isalpha() and letter not in keyDict:
                keyDict[letter] = alphabet[indexCount]
                indexCount+=1
        
        for letter in message:
            if letter.isalpha():
                decodeList.append(keyDict[letter]) 
            else:
                decodeList.append(" ")
        return "".join(decodeList)



s = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(s.decodeMessage(key,message))