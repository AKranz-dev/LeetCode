class Solution:
    def equalFrequency(self, word: str) -> bool:      

        #Replaces a letter with a #
        for letter in set(word):
            freqDict = {}
            temp = word.replace(letter,'#',1)


            #Checks the frequency of all remaning letters, by adding them to a dictionary
            for letter in set(temp):
                if letter != '#':
                    freqDict[letter] = temp.count(letter)
            
                
            #Checks count of unique frequencies in the dictionary
            if len(set(freqDict.values())) == 1:
                return True
                
        return False






word = "abbcc"
s = Solution()
print(s.equalFrequency(word))

#Output true, expected false