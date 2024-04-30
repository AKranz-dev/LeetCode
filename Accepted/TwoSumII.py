class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        res = []
        p1 = 0
        p2 = (len(numbers)-1)

        #Removing list items that are impossible to be the solution, saves a small amount of time against Leetcode's problem set.
        for item in reversed(res):
            if item > target:
                res.remove(item)
            else:
                break
        
        #Two pointer solution
        while True:
            if numbers[p1] + numbers[p2] != target:
                if numbers[p1] + numbers[p2] < target:
                    p1 +=1
                elif numbers[p1] + numbers[p2] > target:
                    p2 -=1
            else:
                res.append(p1+1)
                res.append(p2+1)
                return res



            



numbers = [2,7,11,15]
target = 9

a = Solution()
print(a.twoSum(numbers,target))