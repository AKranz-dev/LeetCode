class Solution:
    def minimumSum(self, num: int) -> int:
        numList = []
        resultList1 = []
        resultList2 = []

        for nu in str(num):
            numList.append(int(nu))
        sorted = numList.sort()
        
        resultList1.append(str(numList[0]))
        resultList1.append(str(numList[2])) 
        result1 = "".join(resultList1)
        print(result1)

        resultList2.append(str(numList[1]))
        resultList2.append(str(numList[3]))
        result2 = "".join(resultList2)
        print(result2)

        output = int(result1) + int(result2)

       
       
        return output


s = Solution()

num = 2932
print(s.minimumSum(num))

#After sorting it's: 2239
#You would think that 22 and 39 would make the smallest sum. But actually, you need to distribute the two smallest numbers to the others to achieve the lowest possible sum.
