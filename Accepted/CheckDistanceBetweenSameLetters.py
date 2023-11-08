class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:

        distanceDict = {}
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for num,letter in zip(distance,alphabet):
            distanceDict[letter] = num
        
        
        letterList = []
        counter = 0

        for letter in s:
            if letter not in letterList:
                letterList.append(letter)
                index1 = s.index(letter)
                index2 = s.index(letter,index1+1)
                actualDistance = (index2 - index1) - 1
                
                print(letter,index1,index2,actualDistance)

                if distanceDict[letter] != actualDistance:
                    return False
                
                counter +=1
        return True
        
        
a = Solution()
s = "zz"
distance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
print(a.checkDistances(s,distance))
