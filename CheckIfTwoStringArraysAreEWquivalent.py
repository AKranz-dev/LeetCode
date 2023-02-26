class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        word1List = []
        word2List = []

        join1List = []
        join2List = []

        word1Dict = {}
        word2Dict = {}
        falseCount = 0
        



        for word in word1:
            join1List.append(word)
        
        for word in word2:
            join2List.append(word)

        if "".join(join1List) != "".join(join2List):
            return False




        for word in word1:
            for letter in word:
                word1List.append(letter)
        
        for word in word2:
            for letter in word:
                word2List.append(letter)
        

        for letter in word1List:
            if letter not in word1Dict:
                word1Dict[letter] = word1List.count(letter)
        

        for letter in word2List:
            if letter not in word2Dict:
                word2Dict[letter] = word2List.count(letter)



        for item in word1Dict:
            if item not in word2Dict:
                return False
        
        for item in word2Dict:
            if item not in word1Dict:
                return False


        for item in word1Dict:
            if word1Dict[item] != word2Dict[item]:
                falseCount =1
        if falseCount == 1:
            return False
        else:
            return True

        








word1 = ["ab", "d"]
word2 = ["a", "bc"]
s = Solution()
print(s.arrayStringsAreEqual(word1,word2))