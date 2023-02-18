class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        counter = 0
        letterDict = {}
        newList = []

        for letter in s:
            letterDict[indices[counter]] = letter
            counter +=1

        myKeys = list(letterDict.keys())
        myKeys.sort()
        sortedDict = {i: letterDict[i] for i in myKeys}
        for key in sortedDict:
            newList.append(sortedDict[key])
        finalString = "".join(newList)
        return finalString




    


a = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(a.restoreString(s,indices))