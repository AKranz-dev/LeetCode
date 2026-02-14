class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        returnList = []
        temp = 0

        if k ==0:
            for i in range(len(code)):
                returnList.append(0)
            return returnList
        
        if k>0:
            #Iterate through each position
            for num in range(0,len(code)):

                if num+(k+1) > len(code):
                    print("WRAPPING list number {}".format(code[num]))
                    
                    wrap = k - (len(code) - (num+1))
                    #print("Wrapping amount: {}".format(wrap))

                    #from current position to end of list
                    for i in range(num+1,len(code)):
                        #print("adding these: {}".format(code[i]))
                        temp += code[i]
                    
                    #from beginning to wrap
                    for i in range(0,wrap):
                        temp += code[i]
                    returnList.append(temp)
                    temp = 0
                
                else:
                    #Adds all remaining numbers from current position
                    for i in range(num+1,num+k+1):
                        temp += code[i]
                    returnList.append(temp)
                    temp = 0
        
        
        if k<0:
            for num in range(0,len(code)):
                
                
                if num-abs(k) < 0:
                    wrap = (abs(k)-num)
                    #print("WRAPPING list number {}".format(code[num]))
                    #print("Wrapping amount: {}".format(wrap))
                    
                    #from beginning to current position
                    for i in range(0,num):
                        #print("adding this: {}".format(code[i]))
                        temp += code[i]
                    
                    #from end of list to wrap
                    for i in range(len(code)-wrap, len(code)):
                        #print("adding this: {}".format(code[i]))
                        temp += code[i]
                    returnList.append(temp)
                    temp = 0
                
                else:
                    for i in range(num-abs(k),num):
                        temp += code[i]
                    returnList.append(temp)
                    temp = 0

        
        
        return returnList


s = Solution()
code = [2,4,9,3]
k = -2

print(s.decrypt(code, k))
