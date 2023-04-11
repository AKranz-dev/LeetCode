class Solution:
    def reverse(self, x: int) -> int:

        res = []
        symbol = ""


        for item in str(x):
            if item.isnumeric():
                res.append(item)
            else:
                symbol+=item
        
        res.reverse()
        if symbol != "":
            res.insert(0,symbol)
        if int("".join(res)) < (2**31)-1 and int("".join(res)) > -2**31:
            return int("".join(res))
        else:
            return 0

    
x = 1534236469
s = Solution()
print(s.reverse(x))