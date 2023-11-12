class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:


        binDict = {}
        countDict = {}
        returnList = []
        dictValues = []
        sortList = []
        killList = []

        for num in arr:
            if arr.count(num) == len(arr):
                for i in range(0,len(arr)):
                    returnList.append(num)
                return returnList
            
            binNum = bin(num)
            binDict[num] = binNum[2:]
        
        # print(binDict)

        for item in binDict:
           countDict[item] = str(binDict[item]).count('1')
        
        # print(countDict)


        countDict = dict(sorted(countDict.items(), key=lambda item: item[1]))
        

        for value in countDict:
            dictValues.append(countDict[value])


        for entry in countDict:
            if dictValues.count(countDict[entry]) > 1 and entry not in killList:
                
                #retrieve all entries that have the same dict value, sort them, and iterate through appending each to the return list
                for item in countDict:
                    if countDict[item] == countDict[entry]:
                        if arr.count(item)>1:
                            for i in range(0,arr.count(item)):
                                sortList.append(item)
                        else:
                            sortList.append(item)
                        
                        killList.append(item)

                

                sortList.sort()
                # print(sortList)
                
                for thing in sortList:
                    returnList.append(thing)
                
                sortList.clear()
            
            elif dictValues.count(countDict[entry]) < 2:
                returnList.append(entry)
        
        return returnList


#Passing 76/77 testcases. The current issue is that there are two same numbers in the input (6144). On line 19, I store the binary value of 6144 into a dictionary using '6144' as the key. The second time 6144 comes around, it gets overwritten.



arr = [9897,785,8844,7607,5898,218,3940,1847,1274,7532,7014,7180,753,6547,8819,7804,6399,79,2928,6516,554,6487,9990,5885,5914,7214,7580,7574,6560,2336,9889,3035,2539,6606,6041,659,600,1578,3740,8566,2124,2584,5996,1490,8064,1164,9054,1853,2339,912,6701,2298,5932,3688,206,4519,6854,4562,5348,8733,2266,85,1636,1674,818,6031,8022,5442,4837,172,3125,9736,3111,4188,658,3692,204,2396,7130,1903,1562,3426,2060,3117,4267,6860,1455,5541,1098,9381,9201,7801,6955,7544,11,1582,5921,8616,4539,523,2731,2193,9580,9744,1411,5857,6507,1879,6573,7882,7848,2772,3277,9449,2249,7540,6430,7895,5708,6144,3293,5229,735,3477,7631,9088,7178,6138,4930,9135,3432,817,6932,164,3652,5053,9075,2964,3852,840,5889,166,2729,583,9976,227,1313,8875,5517,8777,7014,3765,7329,5377,3098,5508,4591,8438,6256,4076,4657,6237,8657,7541,8204,8845,1670,3225,409,58,1061,1700,9274,9982,660,981,6839,5103,9660,2761,4423,1217,5819,4842,1443,3845,7082,7386,9523,1719,2254,5355,7638,6118,6144,9517,8418,6678,1013,9094,3471,8864,7793,381,3373,9366,8382,5369,9591,6221,5557,2378,4059,830,1495,8611,565]
s = Solution()
print(s.sortByBits(arr))
