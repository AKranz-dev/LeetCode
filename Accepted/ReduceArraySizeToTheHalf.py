class Solution:
    def minSetSize(self, arr: list[int]) -> int:

        arrSet = set(arr)
        freqList = []
        temp = 0
        count = 0

        
        #The target length of the array
        target = int(len(arr)/2)
  
        
        #If the length of the set is the same length as the original array, we know the frequency of each number is 1 and therefore can simply return the target
        if len(arrSet) == len(arr):
            return target

        
        #Count frequency of numbers, and add to a list
        for num in arrSet:
            freqList.append(arr.count(num))
        
        #base cases
        if target in freqList:
            return 1
        
        if len(arrSet) == 1:
            return 1
        

        #Return the count of numbers that add up to the target
        #Sort the dictionary by values (highest to lowest), continuously subtract numbers (starting from the highest) until the result is <= (len(arr)/2)

        freqList.sort(reverse=True)


        for item in freqList:
            count +=1
            #print("Checking if {} - {} - {} is <= to {}...".format(len(arr),item,temp,target))
            if len(arr) - item - temp <= target:
                return count
            temp += item
            

        


arr = [1,2,3,4,5,6,7,8,9,10]
s = Solution()
print(s.minSetSize(arr))
