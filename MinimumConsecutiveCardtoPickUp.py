class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        cardList = []
        diffList = []
        
        for card in cards:
            if card not in cardList:
                cardList.append(card)
            else:
                cardList.append(card)

                firstIndex = cards.index(card) #index location of first card
                secondIndex = len(cardList)  #index location of second card
                
                indexDiff = secondIndex-firstIndex
                
                diffList.append(indexDiff)
        
        if len(diffList)>0:
            return min(diffList)
        else:
            return -1
        




s = Solution()
cards = [3,4,2,3,4,7]
print(s.minimumCardPickup(cards))