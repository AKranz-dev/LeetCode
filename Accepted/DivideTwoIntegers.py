class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        

    
        if dividend < 0 and divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            prefix = False

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            dividend = abs(dividend)
            divisor = abs(divisor)
            prefix = True
        
        
        #Edge case
        if (dividend > (2**31)-1 or dividend < -2**31) and (divisor == 1 or divisor == -1):
            if prefix == True:
                return -2**31
            else:
                return (2**31)-1
        
        #Edge case
        if divisor == 1 or divisor == -1:
            if prefix == True:
                return -abs(dividend)
            else:
                return abs(dividend)
        
        #Edge case
        if divisor == dividend:
            if prefix == True:
                return -1
            else:
                return 1

        result = len(range(0,dividend-divisor+1,divisor))
        if prefix == True:
            return -abs(result)
        else:
            return abs(result)

 
            
s = Solution()
dividend = -2147483648
divisor = 2
print(s.divide(dividend,divisor))