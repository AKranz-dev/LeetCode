class Solution:
    def freqAlphabets(self, s: str) -> str:
            
        nums = ["1","2","3","4","5","6","7","8","9","10#","11#","12#","13#","14#","15#","16#","17#","18#","19#","20#","21#","22#","23#","24#","25#","26#"]
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        mapDict = {}
        returnList = []

        stringList = []
        counter = 0
        tempstring = ""
        finalList = []
        tempList = []

        for item in s:
            stringList.append(item)
        
        stringList.reverse()

        for item in stringList:
            if item == "#":
                counter = 2
            else:
                if counter > 0:
                    tempstring = tempstring +  str(item)
                    counter -= 1
                    if counter == 0:
                        for digit in tempstring:
                            tempList.append(digit)
                        tempList.reverse()
                        mystring = "".join(tempList)
                        finalList.append(mystring+"#")
                        tempstring = ""
                        mystring = ""
                        tempList.clear()
                else:
                    finalList.append(item)
        finalList.reverse()
        
        for num in nums:
            mapDict[num]=letters[nums.index(num)]

        
        for item in finalList:
            returnList.append(mapDict[item])
        return "".join(returnList)
        



a = Solution()
s = "10#11#12"
print(a.freqAlphabets(s))

#reverse = 21#11#01