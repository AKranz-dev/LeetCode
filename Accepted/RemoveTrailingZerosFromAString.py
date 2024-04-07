class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        res = ""

        #base case
        if "0" not in num:
            return num
        
        for x in range(len(num)-1,-1,-1):
            if num[x] != "0":
                for i in range(x,-1,-1):
                    res+=(num[i])
                break
        
        return res[::-1]



a = Solution()
num = "51230100"
print(a.removeTrailingZeros(num))