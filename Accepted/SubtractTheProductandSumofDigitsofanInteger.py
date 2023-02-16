class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0

        for digit in str(n):
            product = int(digit)*product
            sum = int(digit)+sum
        return product-sum



s = Solution()
n=234
print(s.subtractProductAndSum(n))