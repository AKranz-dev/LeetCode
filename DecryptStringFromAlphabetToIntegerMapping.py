class Solution:
    def freqAlphabets(self, s: str) -> str:
        #Scan the text
        #If you come across a #, you know the two characters preceeding it belong to the hashtag. Make a note of their index location in the string
        #Add the index locations to a list
        #Scan the text again, and for each character check if it's index is in the list. If not, it belongs to the a-i character set, and can be added to the result
        #If you find a hashtag, capture the chars that are index-1 and index-2 from it and add it to the result

        indexDict = {}
        indexCounter = 1
        hashList = []
        lastIndex = 0

        for char in s:
            charIndex =  s.index(char,lastIndex)
            if char == "#":
                if charIndex not in indexDict:
                    indexDict[indexCounter] = charIndex #Stores the index of the #. The key is a number incrementing by 1. So at the end, there will be an entry in the dictionary of the index of every #
                    indexCounter +=1
                    lastIndex = charIndex
        
        lastIndex = 0
        for char in s:
            charIndex =  s.index(char,lastIndex)
            lastIndex = charIndex
            if charIndex+2 in indexDict: #If the index of this character (plus 2) is the index of the hashtag,we know that this char and the next belong to the hashtag
                hashList.append(char)
                hashList.append(s[charIndex+1]) #adds the hashtag numbers to a list
                newString = "".join(hashList)
                print(newString)
        
        print(indexDict)
            



a = Solution()
s = "10#11#12"
print(a.freqAlphabets(s))