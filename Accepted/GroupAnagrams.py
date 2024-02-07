class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        tempList = []
        finalList = []
        res = []
        kill = 0
        wordDict = {}

 
        emptys = strs.count("")
        for i in range(emptys):
            strs.remove("")
        

        #Creates our key dictionary, which we check the words in strs against
        for word in strs:
            tempList = []
            for letter in word:
                tempList.append(letter)
            if ("".join(sorted(tempList))) not in wordDict.keys():
                wordDict["".join(sorted(tempList))] = []
        
        print(wordDict)


        #Iterate through each word in strs, comparing the word to every key until a match is found. When a match is found, add the word to the dictionary entry that matches the corresponding key. 
        for word in strs:
            print("Checking {} against the key".format(word))
            for item in wordDict:
                kill = 0
                print("Using {} as key".format(item))
                if len(word) != len((item)):
                    continue
                for letter in word:
                    if word.count(letter) != item.count(letter):
                        kill = 1
                        break
                    if letter not in item:
                        kill = 1
                        break
                if kill == 0:
                    wordDict[item].append(word)
                    break
        print(wordDict)
        for key in wordDict:
            res.append(wordDict[key])
        
        if emptys>0:
            for i in range(emptys):
                finalList.append("")
            res.append(finalList)
        return(res)

                    
                    




a = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(a.groupAnagrams(strs))

