class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        allSubs = []
        counter = 0

        #Capture substrings
        while len(arr) > 0:
            for x in range(len(arr)):
                sub = arr[0:x+1]
                allSubs.append(sub)
            arr.pop(0)
        print(allSubs)

        #Sum the substrings
        for x in range(len(allSubs)):
            allOdd = False
            
            if len(allSubs[x]) == 2:
                for y in range (len(allSubs[x])):
                    if allSubs[x][y] %2 == 0:
                        break
                    if y == len(allSubs[x])-1:
                        allOdd = True

                if allOdd == True:
                    print("Skip ({})".format(allSubs[x]))
                    continue
            

            if sum(allSubs[x]) % 2 !=0:
                counter +=1
        
        return counter
            



s = Solution()
arr = [1,2,3,4,5,6,7]

print(s.numOfSubarrays(arr))