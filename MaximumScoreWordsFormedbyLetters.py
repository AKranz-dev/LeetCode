class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:

        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        scoreDict = {}
        res = 0
        

        #Add the alphabet and their scores to a dictionary
        for item,letter in zip(score,alphabet):
            scoreDict[letter] = item

        
        words.sort(key=lambda s: len(s))

        
        #Iterate through words, check if the word contains scoring letters
        for word in words:
            canScore = True
            print("Next word is {}".format(word))

            #Check that we have enough letters left over to make the next word
            for letter in word:
                if letter not in letters:
                    print("Not enough letters left for this word")
                    canScore = False
                    break
            
            if canScore == True:
                #Iterate through unique letters in the word, adding up the score. Then removes the used letters from the letters list.
                temp = 0
                for letter in set(word):
                    temp += scoreDict[letter]
                    letters.remove(letter)
                    print("Removed '{}' from the letters list...".format(letter))
                
                print("Letters list is now {}".format(letters))
                res+=temp
            
            else:
                continue
            
        return res


#====================================================================================================


#Score every word, sort by highest score
#If there are 2 words with same score, sort so that the shortest words with the same score come first (to use the least letters from our letter bank)
#Iterate through the list scoring and removing letters

#Or alteriatively, Divide the score by the number of letters (score per letter), and then sort the list of words by the highest score per letter and iterate until you run out of letters

#The above 2 approaches dont work for every use case - I would have to build both solutions and just return the max score from both - which is likely to exceed the runtime limit

s = Solution()
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(s.maxScoreWords(words,letters,score))