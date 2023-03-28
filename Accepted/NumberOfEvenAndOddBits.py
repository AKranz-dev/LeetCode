class Solution:
    def evenOddBit(self, n: int) -> list[int]:

        evenCounter = 0
        oddCounter = 0
        returnList = []
        binList = []
        cleanList = []



        for num in str(bin(n)):
            binList.append(num)
        

        binList.reverse()
        
        for item in binList:
            if item.isnumeric():
                cleanList.append(item)
            else:
                break

        for i in range(0,len(cleanList)):
            if cleanList[i] == "1":
                if i == 0 or i%2 == 0:
                    evenCounter+=1
                else:
                    oddCounter +=1
        
        
        returnList.append(evenCounter)
        returnList.append(oddCounter)

        return returnList


        
        #starting from the righgt of the binary number, if there is a 1 you will take note of the index its on, and keep count of the even or odd indices
        




n = 17
s = Solution()
print(s.evenOddBit(n))