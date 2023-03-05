class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        newNum = 0
        numList = []

        for i in range (0,len(num)):
            if num[i] == '6':
                newNum = num[:i] + '9' + num[i+1:]
            else:
                newNum = num[:i] + '6' + num[i+1:]
            numList.append(newNum)
        
        for i in range(0,len(numList)):
            numList[i] = int(numList[i])
        
  
        if max(numList) > int(num):
            return max(numList)
        else:
            return int(num)






num = 9669
s = Solution()
print(s.maximum69Number(num))