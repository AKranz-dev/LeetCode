class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:


        keyStack = []
        roomsVisited = []
        
        for item in rooms[0]:
            keyStack.append(item)
        roomsVisited.append(0)           

        while len(keyStack) > 0:

            for key in keyStack:
                keyStack.remove(key)
                roomsVisited.append(key)
                
                for item in rooms[key]:
                    if item not in roomsVisited and item not in keyStack:
                        keyStack.append(item)

        
        return len(roomsVisited) == len(rooms)




s = Solution()
rooms = [[1],[2],[3],[]]
print(s.canVisitAllRooms(rooms))