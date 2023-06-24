class Solution:
    def equalFrequency(self, word: str) -> bool:

        letterDict = {}

        for letter in set(word):
            letterDict[letter] = word.count(letter)
        
        print(letterDict)

        #If the word is made up of a single letter, return True
        if len(set(word)) == 1:
            return True
        
        #If all letters have the same frequency, and that frequency is 1 (e.g. b,a,c)
        if len(set(letterDict.values())) == 1 and word.count(letter) == 1:
            return True
        
        #If all letters have the same frequency, and that frequency is not 1 (e.g. aa,bb)
        elif len(set(letterDict.values())) == 1:
            return False
       
        #If there are 3 different frequencies of letters, impossible to delte a single letter to equalize freqneucies
        elif len(set(letterDict.values())) >2:
            return False
        
        #If there are 2 different frequencies
        elif len(set(letterDict.values())) == 2:

            #If there are multiple letters at the max frequency and multiple letters at the min frequency, return false as deleting one occurence of one letter will not equalize (e.g. aa,bb,c,d)
            if sum(value == max(letterDict.values()) for value in letterDict.values()) > 1 and sum(value == min(letterDict.values()) for value in letterDict.values()) > 1:
                return False
            

            #If there are multiple letters at the max frequency, but the min frequency is a single letter and that frequency is 1, we can just delete the single letter. (e.g. abbcc)
            if sum(value == max(letterDict.values()) for value in letterDict.values()) > 1 and sum(value == min(letterDict.values()) for value in letterDict.values()) == 1 and min(letterDict.values()) == 1:
                return True
            

            #If there are multiple letters at the max frequency, but the min frequency is a single letter and that frequency is NOT 1, we can not just delete the single letter. (e.g. aaaa,bbbb,ccc)
            if sum(value == max(letterDict.values()) for value in letterDict.values()) > 1 and sum(value == min(letterDict.values()) for value in letterDict.values()) == 1 and min(letterDict.values()) != 1:
                return False


            
            #Check that the max frequency -1 equals the other frequency
            if max(letterDict.values()) -1 == min(letterDict.values()):
                return True
            
            #Checks if the count of letters with the min frequency is 1 AND the frequency is 1
            elif sum(value == min(letterDict.values()) for value in letterDict.values()) == 1 and min(letterDict.values()) ==1:
                return True
            
            else:
                return False
        
        
        else:
            return False






word = "aaaabbbbccc"
s = Solution()
print(s.equalFrequency(word))

#Output true, expected false