#https://leetcode.com/problems/longest-common-prefix/solutions/?languageTags=python3

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
#         letterIndex = 0
#         letterList = []
#         for word in strs:
#             print ("checking if {} in {} is equal to {} in {}".format(word[letterIndex], word, strs[strs.index(word)][letterIndex], strs[strs.index(word)+1]))
#             if word[letterIndex] == strs[strs.index(word)+1][letterIndex]:
#                 letterList.append(word[letterIndex])
#                 letterIndex +=1

#                 continue
#             else:
#                 return letterList

# mySolution = Solution()
# strs = ["flower","flow","flight"]
# print(mySolution.longestCommonPrefix(strs))

#Using a set to capture the matching letters. Wont work if there is a common prefix with repeating letters.
# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         lettersSet= set()
#         newList = []
#         shortestWord = min(strs, key=len)
#         strs.remove(shortestWord)
#         for letter in shortestWord:
#             for word in strs:
#                 print("Checking if {} in {} is equal to {} in {}".format(letter, shortestWord, word[shortestWord.index(letter)] ,word))
#                 if letter == word[shortestWord.index(letter)]:
#                     lettersSet.add(letter)
#                 else:
#                     if len(lettersSet) == 0:
#                         lettersList = list(lettersSet)
#                         returnString = "".join(lettersList)
#                         return returnString
#                     else:
#                         lettersSet.remove(letter)
#                         lettersList = list(lettersSet)
#                         returnString = "".join(lettersList)
#                         return returnString
#         return lettersSet
            




# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
        

#         #For each letter in the shortest word:
#             #while stillmatching=true
#                 #for each word in strs:
#                     #If the letter in the word at the same index as our shortest word letter is the same
#                     #else, stop checking - stillmatching=false
#                 #add the letter to a list
        
#         letterList = []

#         if "" in strs:
#             return ""
#         if len(strs) == 1:
#             returnString = "".join(strs)
#             return returnString
#         else:
#             shortestWord = min(strs, key=len)
#             strs.remove(shortestWord)
#             for letter in shortestWord:
#                 for word in strs:
#                     if letter == word[shortestWord.index(letter)]:  #Looks for the first occurence of the letter in the shortest word.
#                         i=1
#                     else:
#                         if len(letterList)>0:
#                             returnString = "".join(letterList)
#                             return returnString
#                         else:
#                             return ""
#                 letterList.append(letter)
#             return shortestWord
        
            
                

# mySolution = Solution()
# strs = ["aa","ab"]
# print(mySolution.longestCommonPrefix(strs))










#BEST SOLUTION HERE - passing 119/124 test cases
# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
        

#         #For each letter in the shortest word:
#             #while stillmatching=true
#                 #for each word in strs:
#                     #If the letter in the word at the same index as our shortest word letter is the same
#                     #else, stop checking - stillmatching=false
#                 #add the letter to a list
        
#         letterList = []
#         indexDict = {}

#         if "" in strs:
#             return ""
#         if len(strs) == 1:
#             returnString = "".join(strs)
#             return returnString
#         else:
#             shortestWord = min(strs, key=len)
#             strs.remove(shortestWord)
#             print("Shortest word is {}. Removing from list of words...".format(shortestWord))
#             for letter in shortestWord:
#                 for word in strs:
#                     print("Checking if {} in {} matches {} in {}".format(letter,shortestWord,word[shortestWord.index(letter)],word))
#                     if letter == word[shortestWord.index(letter)]:  #Looks for the first occurence of the letter in the shortest word. Need to use the dictionary I made in ValidParenthesis to keep a running track where the letters occur in the word.
#                         i=1
#                         print("it does!")


#                         if shortestWord.count(letter) > 1:
#                             print("Checking if {} exists in the dictionary".format(letter))
                            
#                             if letter in indexDict.keys():
                                
#                                 print("It does! And has the value of {}. Meaning that the index location of {} in {} is {}".format(indexDict[letter], letter, shortestWord, indexDict[letter]))
#                                 print("Checking if {} is equal to {} in {}".format(letter,word[shortestWord.index(letter,indexDict[letter]+1)],word))
                                
#                                 if letter == word[shortestWord.index(letter,indexDict[letter]+1)]:
#                                     i=1
#                                 else:
#                                     returnString = "".join(letterList)
#                                     return returnString
#                             else:
#                                 print("Adding {} to the dictionary with a value of {}".format(letter,shortestWord.index(letter)))
#                                 indexDict[letter] = shortestWord.index(letter)
                    
                    
#                     else:
#                         if len(letterList)>0:
#                             returnString = "".join(letterList)
#                             return returnString
#                         else:
#                             return ""
#                 letterList.append(letter)
#             return shortestWord



#Different approach, only passing 97/124
        
        # wordLength = 50000
        # letterList = []
        # counter = 0
        # indexCounter = 0
        # countList = []
        # shortestPrefix = 50000
        # returnList = []

        # for str in strs:
        #     if len(str) < wordLength:    
        #         wordLength = len(str)
        #         shortestWord = str
        # print(shortestWord)
        # print(wordLength)
        
        # if len(strs) == 1:
        #     return shortestWord

        # for word in strs:
        #         if word != shortestWord:
        #             print("Now checking word {}...".format(word))
        #             indexCounter = 0
        #             for i in range(0,wordLength):
        #                 print("Checking if {} matches {}...".format(word[indexCounter],shortestWord[indexCounter]))
        #                 if word[indexCounter] == shortestWord[indexCounter]:
        #                     letterList.append(shortestWord[indexCounter])
        #                     indexCounter+=1
        #                 else:
        #                     letterList.append("#")
        #                     break
        #             letterList.append("#")
        
        # print(letterList)

        # for item in letterList:
            
        #     if item != "#":
        #         countList.append(item)
        #     else:
        #         print("Checking if the length of curent prefix {} is less than {}".format(len(countList),shortestPrefix))
        #         if len(countList) < shortestPrefix and len(countList) !=0:
        #             shortestPrefix = len(countList)
        #             returnList.clear()
        #             for item in countList:
        #                 returnList.append(item)
        #         countList.clear()
        # return "".join(returnList)
        

     
mySolution = Solution()
strs = ["abab","aba","abc"]
print(mySolution.longestCommonPrefix(strs))

