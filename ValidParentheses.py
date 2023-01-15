#https://leetcode.com/problems/valid-parentheses/discussion/

class Solution:
    def isValid(self, s: str) -> bool:


        #First submission: 87/92 tests passed
        #===============================================================================================================================================================
        #Counters used to assign a number to the keys in smybolDict
        openBracketCounter = 0
        openParenthesisCounter = 0
        openCurlyCount = 0
        
        closedBracketCounter = 0
        closedParenthesisCounter = 0
        closedCurlyCount = 0

        symbolDict = {}

        currentOpenParenthLocation = 0
        currentOpenBracketLocation = 0
        currentOpenCurlyLocation = 0

        currentClosedParenthLocation = 0
        currentClosedBracketLocation = 0
        currentClosedCurlyLocation = 0



        for letter in s:

            #Parenthesis
            #Looks for opening brackets, captures index location with key being it's symbol and a number counter.
            if letter == "(":
                symbolDict[letter+str(openParenthesisCounter)]=s.index(letter,currentOpenParenthLocation)
                currentOpenParenthLocation=s.index(letter,currentOpenParenthLocation)+1 #takes the value of the index of the last detected parenthesis, and adds one. Start searching from this location.
                openParenthesisCounter+=1

                #If the letter is not the first or last in the list
                if s.index(letter) > 0 and s.index(letter) < len(s)-1:
                    #Checks if the next letter is a closing bracket of the opposite type
                    if s[s.index(letter)+1] == "}" or s[s.index(letter)+1] == "]":
                        return False

            #Looks for closing brackets, captures index location with key being it's symbol and a number counter.
            if letter == ")":
                symbolDict[letter+str(closedParenthesisCounter)]=s.index(letter,currentClosedParenthLocation)
                currentClosedParenthLocation=s.index(letter,currentClosedParenthLocation)+1 #takes the value of the index of the last detected closed parenthesis, and adds one. Start searching from this location.

                #First, checks if an opening bracket exists in the dictionary at the same number as the closing
                if "("+str(closedParenthesisCounter) in symbolDict:
                    #Checks if the index value of the opening brakcet (at the same number as the closing ({1, {2, {3, etc.) is LESS than that of the closing, that means the opening came before the closing and is valid.
                    if symbolDict["("+str(closedParenthesisCounter)] < symbolDict[")"+str(closedParenthesisCounter)]:
                        closedParenthesisCounter+=1
                    else:
                        return False
                else:
                    return False
            


            #Brackets
            if letter == "[":
                symbolDict[letter+str(openBracketCounter)]=s.index(letter,currentOpenBracketLocation)
                currentOpenBracketLocation=s.index(letter,currentOpenBracketLocation)+1 #takes the value of the index of the last detected parenthesis, and adds one. Start searching from this location.
                openBracketCounter+=1

                #If the letter is not the first or last in the list
                if s.index(letter) > 0 and s.index(letter) < len(s)-1:
                    #Checks if the next letter is a closing bracket of the opposite type
                    if s[s.index(letter)+1] == "}" or s[s.index(letter)+1] == ")":
                        return False

            #Looks for closing brackets, captures index location with key being it's symbol and a number counter.
            if letter == "]":
                symbolDict[letter+str(closedBracketCounter)]=s.index(letter,currentClosedBracketLocation)
                currentClosedBracketLocation=s.index(letter,currentClosedBracketLocation)+1 #takes the value of the index of the last detected closed parenthesis, and adds one. Start searching from this location.

                #First, checks if an opening bracket exists in the dictionary at the same number as the closing
                if "["+str(closedBracketCounter) in symbolDict:
                    #Checks if the index value of the opening brakcet (at the same number as the closing ({1, {2, {3, etc.) is LESS than that of the closing, that means the opening came before the closing and is valid.
                    if symbolDict["["+str(closedBracketCounter)] < symbolDict["]"+str(closedBracketCounter)]:
                        closedBracketCounter+=1
                    else:
                        return False
                else:
                    return False        

           
           
            #Curly
            if letter == "{":
                symbolDict[letter+str(openCurlyCount)]=s.index(letter,currentOpenCurlyLocation)
                currentOpenCurlyLocation=s.index(letter,currentOpenCurlyLocation)+1 #takes the value of the index of the last detected parenthesis, and adds one. Start searching from this location.
                openCurlyCount+=1

                #If the letter is not the first or last in the list
                if s.index(letter) > 0 and s.index(letter) < len(s)-1:
                    #Checks if the next letter is a closing bracket of the opposite type
                    if s[s.index(letter)+1] == "]" or s[s.index(letter)+1] == ")":
                        return False


            #Looks for closing brackets, captures index location with key being it's symbol and a number counter.
            if letter == "}":
                symbolDict[letter+str(closedCurlyCount)]=s.index(letter,currentClosedCurlyLocation)
                currentClosedCurlyLocation=s.index(letter,currentClosedCurlyLocation)+1 #takes the value of the index of the last detected closed parenthesis, and adds one. Start searching from this location.

                #First, checks if an opening bracket exists in the dictionary at the same number as the closing
                if "{"+str(closedCurlyCount) in symbolDict:
                    #Checks if the index value of the opening brakcet (at the same number as the closing ({1, {2, {3, etc.) is LESS than that of the closing, that means the opening came before the closing and is valid.
                    if symbolDict["{"+str(closedCurlyCount)] < symbolDict["}"+str(closedCurlyCount)]:
                        closedCurlyCount+=1
                    else:
                        return False
                else:
                    return False

            
            # #If the letter is not the first or last in the list
            # if s.index(letter) > 0 and s.index(letter) < len(s)-1:
            #     #Checks if symbols at -1 and +1 index are opening and closing respectively - and that the letter in the middle is not the same type - curlys
            #     if s[s.index(letter)-1] == "{" and s[s.index(letter)+1] == "}" and letter != "{" and letter !="}":
            #         return False
            #     #Checks if symbols at -1 and +1 index are opening and closing respectively - and that the letter in the middle is not the same type - brakcets
            #     elif s[s.index(letter)-1] == "[" and s[s.index(letter)+1] == "]" and letter != "[" and letter !="]":
            #         return False
            #     #Checks if symbols at -1 and +1 index are opening and closing respectively - and that the letter in the middle is not the same type - parenthesis
            #     elif s[s.index(letter)-1] == "(" and s[s.index(letter)+1] == ")" and letter != "(" and letter !=")":
            #         return False

        
        if openParenthesisCounter == closedParenthesisCounter and openBracketCounter == closedBracketCounter and openCurlyCount == closedCurlyCount:
            return True
        
#===============================================================================================================================================================








mySolution = Solution()
s="[([]])"
print(mySolution.isValid(s))


#Read through S
#If you see an open bracket, capture and store its index, with the key being it's symbol and assign it a number (e.g. {1, {2, {3, etc.)
#Continue reading along
#If you see a closing bracket, captur its index location, with the key beign it's symbol and assign it a number (e.g. {1, {2, {3, etc.)
#Compare the index of the openning to the close. If closing brakcet comes after opening (with the corresponding number), then continue
#First submission: 87/92 tests passed


#Using a "stack"
#Read through S
#If you see an open bracket, capture and store its index, with the key being it's symbol and assign it a number (e.g. {1, {2, {3, etc.) and add it to a list myList = [{1, {2, {3]
#Continue reading along
#If you see a closing brakcet, capture its index location, with the key being it's symbol and assign it a number (e.g. {1, {2, {3, etc.) and remove the corresponding value from the list. (e.g. found }1, so we remove {1 from the list leaving {2, and {3)
#At the end, the list should be empty, and return true. If it's not, return false.

#I dont think it will work if s="([)]" - it would simply add bother openers to the list and then remove them.
#The stack method I described is essentially a method to keep a count of all the openers and and count of all the closers and check if their equal. (With the additional check to make sure closers come after openers)
#What I also need to check if that an opening [ bracket did not come before the subsequent closing parenthesis. To solve s="([)]".
#No I actually need to check that a bracket of another type, either [ or {, either open or closed, is not directly in between two parentheses. For example, ([) or (])
    #For each symbol in s (except the first and last symbol), check the value at the -1 and +1 index locaiton of that symbol
    #If -1 is an openeing symbol AND +1 is a closing symbol, return False. This will catch {[}, or ([), or [(]. 
    #However, it doesnt account for this --> (()) - so they key is to make sure that -1 and +1 are not the same symbol as the one being checked. So that (()) passes but ([) fails and returns 'False'.

    #Where should I add this check? Outside of the other checks?





#1.14
#90/92 test cases passed
#[([]]) is failing. Perhaps instead of checking for mating symbols at -1 and +1 index location of the letter, instead just determine if it's an opening or closing symbol and check for that.
#Perhaps each time we see an opening symbol (we make sure its not the first or last) and then we check if symbol at the +1 index location is not a closing bracket of the oother types such as } or ]. If so, return false.
#I think the real issue here is that we need to validate nested parenthesis - in that if there is an opening symbol, there should be even number of opening and closing symbols up until the closing symbol of the original type.
#[([]]) in this example, the number of opening symbols does not equal the number of closing symbols in 2 places
#How to code:
    #If letter is an opening symbol, for each letter in s starting at the index position of the current letter, keep track of number of opening and closing symbols until you find the closing smybol of the same type. 
    #Compare the number of opening and closing symbols and check if they're equal. If not, return False.