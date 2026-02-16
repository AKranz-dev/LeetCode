class Solution:
    def smallestNumber(self, pattern: str) -> str:

        res = []
        counter = 0
        lastItem = pattern[0]


        for x in range(len(pattern)):
            print("Now checking pattern[{}]".format(x))
            counter = 1

            if x == 0:
                if pattern[x] == "I":
                    res.append(1)
                    lastItem = "I"
                    continue
                else:
                    res.append(2)
                    lastItem = "D"
                    continue
            
            #If last item was an I, I need to append a larger number than last
            #This number may already exist, so I first check if the number exists, and then add 1 to it until its a unique number to the result list
            if lastItem == "I":
                if (res[x-1]+1) in res:
                    print("I-COLLISION")
                    while (res[x-1] + counter) in res:
                        counter +=1
                res.append(res[x-1] + counter)
                print("Pattern[{}] was {} and value {}, so I'm appending {}".format(x-1,pattern[x-1],res[x-1],res[x-1] + counter))
                print(res)
           
            elif lastItem == "D":
                if (res[x-1])-1 in res:
                    print("D-COLLISION")
                    
                    while (res[x-1]) - counter in res:
                        counter += 1
                        if (res[x-1]-counter) == 0:
                            res[x-1] = res[x-1]+1
                            break
                counter = 1
                res.append(res[x-1] - counter)
                print("Pattern[{}] was {} and value {}, so I'm appending {}".format(x-1,pattern[x-1],res[x-1],res[x-1] - counter))
                print(res)
            lastItem = pattern[x]
        return str(res)





s = Solution()
pattern = "IIIDIDDD"

print(s.smallestNumber(pattern))