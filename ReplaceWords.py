class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        
        dictionary = sorted(dictionary,key=len)

        #Passing 85/127

        # for word in dictionary:
        #     tempstring = ""
            
        #     #Iterate through the sentence, creating substrings the length of the key word we're looking for
        #     for i in range(len(sentence)):
        #         tempstring = sentence[i:i+(len(word))]

                
        #         #Check for a match to the word from the dict
        #         if tempstring == word:
                    
                    
        #             #Iterate through all letters after the matched word, looking for a space - OR if its the end of the sentence
        #             for x in range(i,len(sentence)):
        #                 if sentence[x] == " ":
        #                     print(sentence[i:x])
        #                     sentence = sentence.replace(sentence[i:x],word)
        #                     break
                        
        #                 #Check if we've reached the end of the sentence
        #                 elif x == len(sentence)-1:
        #                     print(sentence[i:x+1])
        #                     sentence = sentence.replace(sentence[i:x+1],word)
        #                     break
        # return sentence

#Passing 108/127
#====================================================================================================

        for word in dictionary:
            tempString= ""
            i=0
            
            #Iterate through the sentence
            for letter in sentence:
                i+=1
                
                #Capture a word
                if letter != " " and i != len(sentence):
                    tempString += letter
                
                #Space is found, check the the tempString length is at least that of the word
                else:
                    if len(tempString)<len(word):
                        tempString = ""
                    
                    #Iterate through the tempstring, checking that it matches the word
                    else:
                        
                        if tempString[0:len(word)] == word and i == len(sentence):
                            print(tempString[0:len(word)])
                            tempString +=sentence[len(sentence)-1]
                            sentence = sentence.replace(tempString,word)
                            tempString = ""                        

                        elif tempString[0:len(word)] == word:
                            print(tempString[0:len(word)])
                            sentence = sentence.replace(tempString,word)
                            tempString = ""                        
                        else:
                            tempString = ""
        
        return sentence



                
                #Check for a match to the word from the dict
                # if tempString == word:
                    
                    
                #     #Iterate through all letters after the matched word, looking for a space - OR if its the end of the sentence
                #     for x in range(i,len(sentence)):
                #         if sentence[x] == " ":
                #             print(sentence[i:x])
                #             sentence = sentence.replace(sentence[i:x],word)
                #             break
                        
                #         #Check if we've reached the end of the sentence
                #         elif x == len(sentence)-1:
                #             print(sentence[i:x+1])
                #             sentence = sentence.replace(sentence[i:x+1],word)
                #             break
        # return sentence





s = Solution()
dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(s.replaceWords(dictionary,sentence))