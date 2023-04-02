class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:

        tableList = []
        totalTables = set()
        tempDict = {}
        foodType = set()
        tempList = []
        returnList = []

        for order in orders:
            if order[2] not in tableList:
                tableList.append(order[2])
            totalTables.add(int(order[1]))
            foodType.add(order[2])
        
        tableList.sort()
        tableList.insert(0,"Table")
        returnList.append(tableList)
        
        
        for table in sorted(totalTables):
            for order in orders:
                if order[1] == str(table):
                    if order[2] not in tempDict:
                        tempDict[order[2]] =1
                    else:
                        tempDict[order[2]] +=1
            # print("Table {} orders are {}".format(table,tempDict))    
            
            tempList.append(str(table))
            for food in sorted(foodType):
                if food in tempDict:
                    tempList.append(str(tempDict[food]))
                else:
                    tempList.append('0')
            
            returnList.append(tempList)
            # print(tableList)
            # print(tempList)
            tempDict = {}
            tempList = []
        return returnList

            
                



            
                        




s = Solution()
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(s.displayTable(orders))