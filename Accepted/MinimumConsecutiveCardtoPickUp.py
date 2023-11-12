class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:

        #Working solution, time limit exceeded after 57/80 test cases

        # cardList = []
        # indexList = []
        # lowestDiff = 100000000
 

        # #Gather list of cards that have at least a pair in the deck
        # for card in set(cards):
        #     if cards.count(card) > 1:
        #         cardList.append(card)
        
        # if len(cardList) < 1:
        #     return -1

        # #Iterate through each card, noting the index locations of all those - get the shortest difference in index location between all the instances of that card, and store it. Continue until you have checked all cards in the cardList and have the minnimum distance.
        # for card in cardList:
        #     startingIndex = 0
        #     indexList = []
            

        #     #Get the index locations of the card
        #     for i in range(cards.count(card)):
        #         indexList.append(cards.index(card,startingIndex))
        #         startingIndex = (cards.index(card,startingIndex))+1


        #     #Get the shortest distance between 2 indexes
        #     #e.g. [0, 5, 8]
        #     print("Index list for card '{}' is: {}".format(card,indexList))
        #     for x in range(len(indexList)-1):
        #         print("X")
        #         diff = abs(indexList[x]-indexList[x+1])
        #         if diff < lowestDiff:
        #             lowestDiff = diff
        # return lowestDiff+1


        dict = {}
        distance = 1000000

        #If a card is not in the dictionary, add it and set the value to it's index
        for i in range(len(cards)):
            if cards[i] not in dict:
                dict[cards[i]] = i
            #If it is in the dictionary, check the distance between this occurence and the original (i - (dict[cards[i]])). If that value is lower than the current shortest distance, keep it. Update the dictionary to compare any more occurences.
            else:
                if i-(dict[cards[i]]) < distance:
                    distance = i-(dict[cards[i]])
                dict[cards[i]] = i
        
        if distance == 1000000:
            return -1
        else:
            return distance+1
       


s = Solution()
cards = [1,0,5,3]
print(s.minimumCardPickup(cards))