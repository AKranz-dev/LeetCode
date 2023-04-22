class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:


        
        #Working Solution, but only passing 27/48 cases due to Time Limit Exceeded (needs refactoring)

        res = []

        for i in range(len(temperatures)):
            counter = 1
            entryCounter = 0
            
            #Catching the last temperature in the list
            if i == len(temperatures)-1:
                print("Reached the end..appending 0")
                res.append(0)
            
            for entry in temperatures[i+1::]:
                
                print("{} is our source temp".format(temperatures[i]))
                
                if entry > temperatures[i]:
                    print("{} is greater than {}".format(entry,temperatures[i]))
                    print(counter)
                    res.append(counter)
                    break
                
                else:
                    counter+=1
                    entryCounter+=1

                if entryCounter == len(temperatures[i+1::]):
                    print("Reached the end, and cant get hotter")
                    res.append(0)

                    
        
        return res



temperatures = [55,38,53,81,61,93,97,32,43,78]
#Expected - [3,1,1,2,1,1,0,1,1,0]

s = Solution()
print(s.dailyTemperatures(temperatures))