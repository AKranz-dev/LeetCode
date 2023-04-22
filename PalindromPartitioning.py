class Solution:
    def partition(self, s: str) -> list[list[str]]:

        tempList = []
        res = []

        #Create a list of each letter, base case
        for letter in s:
            tempList.append(letter)
        res.append(tempList.copy())

        
        #Checking the whole word as a palindrome:
        if s == s[::-1]:
            tempList.clear()
            tempList.append(s)
            if tempList not in res:
                res.append(tempList.copy())
        

        #Getting the rest
        for i in range(len(s)+1):
            tempList.clear()

            if s[0:i] == "" or s[i:] == "":
                continue

            subString = s[0:i]
            revSubString = subString[::-1]
            # print("Checking if {} is the same as {}".format(subString,revSubString))


            subString2 = s[i:]
            revSubString2 = subString2[::-1]
            # print("Checking if {} is the same as {}".format(subString2,revSubString2))


            if subString == revSubString and subString2 == revSubString2:
                tempList.append(subString)
                tempList.append(subString2)
                if tempList not in res:
                    res.append(tempList.copy())
        
        return res


#Currently assuming I only need to break the string up into 2 partitions exactly, whereas this needs to be dynamic
s = "abbab"
a = Solution()
print(a.partition(s))