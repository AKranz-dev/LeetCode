class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:

        res = []
        for lt,rt in zip(l,r):
            subArray = []
            kill = 0
            diffHold = 0
            
            for num in nums[lt:rt+1]:
                subArray.append(num)
            
            subArray.sort()
            print(subArray)

            
            for i in range(0,len(subArray)-1):
                diff = subArray[i+1] - subArray[i]

                if i == 0:
                    diffHold = diff
                
                if diffHold != diff:
                    kill =1

                diffHold = diff

            
            if kill == 1:
                res.append(False)
            else:
                res.append(True)
        
        return res

        




nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
s = Solution()
print(s.checkArithmeticSubarrays(nums,l,r))