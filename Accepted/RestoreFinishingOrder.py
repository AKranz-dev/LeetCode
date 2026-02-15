class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        
        #copyfriends to new list in order that they finished
        #res=[]
        # for runner in order:
        #     if runner in friends:
        #         res.append(runner)
        # return res
    
        #iterate over order from the end using negative slice, remove elements that are not friends
        for x in range((len(order)-1),-1,-1):
            if order[x] not in friends:
                order.pop(x)
        return order


s = Solution()
order = [1,4,5,3,2]
friends = [5,2]
print(s.recoverOrder(order,friends))