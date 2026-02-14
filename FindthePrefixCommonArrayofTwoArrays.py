class Solution:
    def func(self, n):
      
      finList = []

      #Gets all numbers from 1 to n
      for num in range(1, n+1):
        print(num)
        temp = 0
        
        #Squares the number
        ints = num * num

        #Partitions the squared number into a summed value that will equal the original number
        str_ints = str(ints)
        found = False
        for i in range(1, len(str_ints)):
            left = int(str_ints[:i])
            right = int(str_ints[i:])
            if left + right == num:
                finList.append(num)
                found = True
                break
      
      
      return finList

n=10
s = Solution()
print(s.func(n))