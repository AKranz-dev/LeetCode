class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        counter = 0

        for i in range (low,high+1): 
            left = 0
            right = 0

            num = str(i)

            #Check if the number is even
            if len(num) % 2 == 0:
                split = (len(num))/2
                splitint = int(split)
                
                print("Number is {}, first half is {} and second is {}".format(i,num[0:splitint],num[splitint::]))
                
                for item,thing in zip(num[0:splitint],num[splitint::]):
                    left += int(item)
                    right += int(thing)
                
                
                if left == right:
                    print("MATCH NUMBER {}".format(num))
                    counter +=1

        return counter


        
s = Solution()
low = 1200
high = 1230
print(s.countSymmetricIntegers(low,high))