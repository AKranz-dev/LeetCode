class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        
        
        sequenceList = []

        returnList = []


        nums.sort()
        print(nums)



        # for i in range(0,len(nums)-1):
        #     print("Checking index {} which is number {} against number {}".format(i,nums[i],nums[i+1]))
        #     if nums[i]+1 == nums[i+1] and i != len(nums)-1:
        #         print("Appending {} to the list...".format(nums[i+1]))
        #         numsSequence.append(nums[i])
        #         numsSequence.append(nums[i+1])
        #     elif i == len(nums)-1:
        #         if nums[i-1]+1 == nums[i]:
        #             numsSequence.append(nums[i])
        #         else:
        #             sequenceList.extend(numsSequence)
        #             numsSequence.clear()
        #             sequenceList.append(nums[i])
        #     else:
        #         sequenceList.extend(numsSequence)
        #         numsSequence.clear()

        
        # return sequenceList

#Probably should restart
        for i in range(0,len(nums)):
            #print("checking if {} - {} is equal to k".format(nums[0],nums[i]))
            if abs(nums[0]-nums[i]) == k:
                for item in nums[0:i+1]:
                    sequenceList.append(item)
                start = i+1
                break
        
        for item in sequenceList:
            returnList.append(item)
        
        for num in sequenceList:
            print("Removing {} from Sequence List".format(num))
            nums.remove(num)
        
        sequenceList.clear()
        
        if len(nums)>0:
            s.partitionArray(nums,k)


    

s = Solution()
nums = [3,6,1,2,5]
k = 2
print(s.partitionArray(nums,k))