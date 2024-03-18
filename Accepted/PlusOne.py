class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        
        temp = ""
        res = []

        for item in digits:
            temp += str(item)
        
        temp = int(temp)
        temp +=1


        for char in str(temp):
            res.append(int(char))
        
        return res






        
a = Solution()
digits = [1,2,3]
print(a.plusOne(digits))