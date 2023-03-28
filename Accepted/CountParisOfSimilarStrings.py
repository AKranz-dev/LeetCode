class Solution:
    def similarPairs(self, words: list[str]) -> int:

        counter = 0
        letterDict = {}
        letterSet = set()
        setList = []
        finalList = []
        


        for word in words:
            for letter in word:
                letterSet.add(letter)
            
            for item in letterSet:
                setList.append(item)

            setList.sort()

            final = "".join(setList)
            finalList.append(final)
            
            setList.clear()
            letterSet.clear()
        
        print(finalList)

        for item in finalList:
            for word in finalList:
                if item == word:
                    counter +=1

        
        return int((counter-len(words))/2)

            


s = Solution()
words = ["aba","aabb","abcd","bac","aabc"]
print(s.similarPairs(words))