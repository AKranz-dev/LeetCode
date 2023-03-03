class Solution:
    
    def areNumbersAscending(self, s: str) -> bool:
        numberList = []
        indexCounter = 0

        for word in s.split():
            if word.isnumeric():
                numberList.append(int(word))
        
        for i in range(0,len(numberList)-1):
            if numberList[i+1] <= numberList[i]:
                return False   
        return True


a = Solution()
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
print(a.areNumbersAscending(s))
