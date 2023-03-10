class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        
        numsSequence = []
        sequenceList = []


        nums.sort()
        print(nums)



        for i in range(0,len(nums)-1):
            print("Checking index {} which is number {} against number {}".format(i,nums[i],nums[i+1]))
            if nums[i]+1 == nums[i+1] and i != len(nums)-1:
                print("Appending {} to the list...".format(nums[i+1]))
                numsSequence.append(nums[i])
                numsSequence.append(nums[i+1])
            elif i == len(nums)-1:
                if nums[i-1]+1 == nums[i]:
                    numsSequence.append(nums[i])
                else:
                    sequenceList.extend(numsSequence)
                    numsSequence.clear()
                    sequenceList.append(nums[i])
            else:
                sequenceList.extend(numsSequence)
                numsSequence.clear()

        
        return sequenceList

#Probably should restart

        

    

s = Solution()
nums = [3,6,1,2,5]
k = 2
print(s.partitionArray(nums,k))