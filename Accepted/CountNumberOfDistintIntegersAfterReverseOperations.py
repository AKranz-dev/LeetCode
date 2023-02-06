class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
    
        digitList = []
        newNums = []

        #Iterates through each number in the list, reverses it, and appends it to the list.
        for num in nums:
            for digit in str(num):
                digitList.append(digit)
            reversedNumber = "".join(reversed(digitList))
            newNums.append(int(reversedNumber))
            digitList.clear()
        nums.extend(newNums)
        print(nums)
       
        #Looks for unique numbers
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = "z"
        uniqueInts = len(numDict)
        print(numDict)
        return uniqueInts


s = Solution()
nums = [1,13,10,12,31]
print(s.countDistinctIntegers(nums))



#300 will be 003
#For every digit in the number, if the digit is a 0, do nothing. If you get to a non-zero, then take that number plus the digits after it and add that to the dict.

#Iterate through numbers in the list
#For each num:
    #Iterate through each digit
    #Add each digit to a new list
    #Call the reversed function to reverse the new list
    #