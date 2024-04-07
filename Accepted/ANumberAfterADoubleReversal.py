class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        if num == 0:
            return True
        
        rev = str(num)[::-1]
        
        for x in range(len(rev)):
            if rev[x] != "0":
                reRev = rev[x::]
                break
        
        finalRev = reRev[::-1]

        if int(finalRev) == num:
            return True
        else:
            return False


        


num = 526
a = Solution()
print(a.isSameAfterReversals(num))