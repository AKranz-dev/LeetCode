class Solution:
    def secondHighest(self, s: str) -> int:

        nums = []

        #Add all numbers to a list
        for item in s:
            if item.isnumeric():
                nums.append(item)

        #Remove duplicate numbers from list
        nums = set(nums)

        #Check that a second largest value exists
        if len(nums) <2:
            return -1
        
        #Sort the list
        sortedNums = sorted(nums)

        #Remove first largest value
        sortedNums.remove(max(sortedNums))
        
        #Return new largest value
        return(int(sortedNums[len(sortedNums)-1]))





a = Solution()
s = "dfa12321afd"
print(a.secondHighest(s))