class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        
        temp = 0
        ltcList = []

        if min(satisfaction) <0 and max(satisfaction)<0:
            return 0
        

        while len(satisfaction) > 0:

            print("Satisfaction is now {}".format(satisfaction))

            #If there are no negative values, sort the list and multiply the top numbers
            if min(satisfaction)>=0:
                satisfactionSort = sorted(satisfaction)
                
                for i in range(len(satisfactionSort)):
                    print("temp ({}) + {} * {} = {} ".format(temp,satisfactionSort[i],i+1,temp + satisfaction[i]*(i+1)))
                    temp += (satisfactionSort[i]*(i+1))
                
                ltcList.append(temp)
                return max(ltcList)
            
            
            else:
                #For satisfaction that contains negative values, sort the list to move all negative values to the beginning
                satisfactionSort = sorted(satisfaction)
                
                for i in range(len(satisfactionSort)):
                    print("temp ({}) + {} * {} = {} ".format(temp,satisfactionSort[i],i,temp + satisfactionSort[i]*i))
                    temp += (satisfactionSort[i]*(i+1))
                
                ltcList.append(temp)
                temp = 0
                satisfaction.remove(min(satisfaction))
        
        
        print(ltcList)
        return max(ltcList)





s = Solution()
satisfaction = [-2,5,-1,0,3,-3]
print(s.maxSatisfaction(satisfaction))
#35

#Solution works as follows: 
# If there are negative numbers in the list, sort it to move the negative numbers to the beginning. 
# This will reduce the impact of the negative numbers (as they are multiplied by lower numbers like 0, 1 ,2 etc.). 
# Record the final score into ltcList, and remove the lowest negative number to help further reduce the impact of the negative numbers. Repeat until there are no negative numbers.

#Once there are no negative numbers, simply sort the remaining values so that the largest numbers are multipled with the largest values (e.g. A list of 3,6,9 should be multyipled as 3*1,2*6, and 3*9).
#Record the resulting value in the ltcList, and return the maximum value from the list.
