class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        winnerList = []
        res = []
        index = 0


        for num in nums:
            diff = target - num
            if diff in nums:
                if diff == num and nums.count(diff) == 1:
                    continue
                winnerList.append(diff)
                winnerList.append(num)
                break
        

        for num in winnerList:
            if len(set(winnerList)) == 1:
                res.append(nums.index(num,index))
                index = nums.index(num)+1
            else:          
                res.append(nums.index(num))
        

        return res



nums = [-3,4,3,90]
target = 0
s = Solution()
print(s.twoSum(nums,target))