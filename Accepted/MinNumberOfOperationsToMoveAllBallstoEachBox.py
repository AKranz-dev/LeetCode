class Solution:
    def minOperations(self, boxes: str) -> list[int]:

        moves = 0
        res = []

        for box in range(len(boxes)):
            print("Checking box at index {}".format(box))

            #left to box (not including current)
            for x in range(0,box):
                if boxes[x] == "1":
                    print("Adding a move from the left")
                    moves+=(box - x)
                    print(moves)
            
            # right to box (not including current)
            for y in range(len(boxes)-1,box,-1):
                if boxes[y] == "1":
                    print("Adding a move from the right")
                    moves+=(y - box)
            
            res.append(moves)
            moves = 0
        
        return res

boxes = "110"
s = Solution()
print(s.minOperations(boxes))