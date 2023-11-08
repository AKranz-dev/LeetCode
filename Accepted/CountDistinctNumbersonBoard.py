class Solution:
    def distinctIntegers(self, n: int) -> int:

        tempBoard = []
        board = []
        numList = []
        board.append(n)
        tempBoard.append(n)
        

        while len(board) >=1:
            for num in board:
                for i in range(1,num):
                    if num % i == 1:
                        board.append(i)
                        tempBoard.append(i)
                board.remove(num)


        for num in tempBoard:
            if num not in numList:
                numList.append(num)
        return len(numList)

        
        


s = Solution()
n = 7
print(s.distinctIntegers(n))
#expected 6