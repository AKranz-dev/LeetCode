class Solution:
    def removeDuplicates(self, s: str) -> str:

        charSet = set()
        start = 0

        # for letter in s:
        #     charSet.add(letter)

        # for letter in charSet:
        #     if s.count(letter) > 1:
        #         for i in range (s.count(letter)):
        #             index = s.index(letter,start)
        #             start = index

        #             if s.index(letter,start) == index+1:
        #                 s[index] = ""
        #                 s[s.index(letter,start)] = ""
        # return s
#==================================================
        # sList = []
        # res = []
        # tryAgain = 1
        # success = 0

        
        # for letter in s:
        #     sList.append(letter)
        

        # for i in range(0,len(sList)):

        #     # if i == len(sList)-1:
        #     #     break

        #     print(sList)
        #     print("Checking index {} ({})".format(i,sList[i]))
            
        #     if sList[i] == sList[i+1]:
        #         res.append(sList[i])
        #         res.append(sList[i+1])
                
        #         print("removing {} and {}...".format(sList[i],sList[i+1]))
                
        #         sList.pop(i)
        #         sList.pop(i)

        #         #Need to restart from the beginning of the string at this point.
                
        # return sList
        #==================================================


        #95/106 Time Limit
        sList = []
        i = 0

        
        for letter in s:
            sList.append(letter)
        

        while i < len(sList)-1:
            print(sList)
            print("Checking index {} ({})".format(i,sList[i]))
            
            if sList[i] == sList[i+1]:
                
                print("removing {} and {}...".format(sList[i],sList[i+1]))
                sList.pop(i)
                sList.pop(i)

                
                if len(sList) == 0:
                    return ""
                
                print(sList[i])

                if i > 0:
                    i-=1
                else:
                    i=0
                #Need to restart from the beginning of the string at this point.
            else:
                print("Index {} ({}) is not equal to index {} ({}))".format(i,sList[i],i+1,sList[i+1]))
                i+=1
        sList = ''.join(sList)
        return sList

            

    
a = Solution()
s = "aaaaaaaa"
print(a.removeDuplicates(s))