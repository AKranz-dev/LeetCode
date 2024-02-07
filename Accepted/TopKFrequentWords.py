class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
       
        #I think I should have a seperate dictionary that includes information about which words have the same frequency and need to be checked for alphabetical order (sorted alphabetically)
        #Basically iterate through each dictionary VALUE and check the count of how many times that value is in the dictioanry (tells us how many duplicates there are.) Map the word frequency (for 'love', its 2), to the number of times the frequency appears in wordDict (2 appears twice in wordDict, seeing as the word 'i' also appears twice).
        #Finally, iterate through the words in the sorted dict, check the secon dictiary saying (I know this word appears twice, how many other words appear twice?) to which it will say there are 2 words that appear twice. You can then grab the current and next word, alphabatize them, add them to the res list, and continue iterating until you reach k.

       
       
        wordDict = {}
        freqDict = {}
        tempList = []
        res = []

        for word in words:
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] +=1
        
        sortedDict = dict(sorted(wordDict.items(), key=lambda item: item[1], reverse=True))

        #Create second dictionary to hold count of frequencies
        for word in sortedDict:
            if sortedDict[word] not in freqDict:
                freqDict[sortedDict[word]] = 1
            else:
                freqDict[sortedDict[word]] += 1
        results = list(sortedDict)

       
        for i in range(k):
            #Checks if the frequency appears more than once. If so, grab this word and the next X to perform an alphabet check. To know how many words to grab of the same frequency, it looks at the smallest number between either the number of words we have left to return (k) minus how many we already have returned (i) or the number of words that have the same frequency, and adds all of them.
            if freqDict[sortedDict[results[i]]] > 1 :
                tempList = []
                for x in range(0,freqDict[sortedDict[results[i]]]):
                    tempList.append(results[i+x])
                sortedList = sorted(tempList)
            
                if k == 1:
                    res.append(sortedList[0])
                else:
                    for l in range(min(k-i,len(sortedList))):
                        res.append(sortedList[l])
                
                freqDict[sortedDict[results[i]]] = -1
            elif freqDict[sortedDict[results[i]]] != -1:
                res.append(results[i])
        return(res)
        
        


a = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 3
print(a.topKFrequent(words,k))