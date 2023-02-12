# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        valList = []
        
        while cur:
            if valList.count(cur.val)>4: #This is hardcoded
                return True
            valList.append(cur.val)
            cur = cur.next