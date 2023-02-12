# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next       
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        valueList = []

        if cur.val is None:
            return -1

        while cur is not None:
            valueList.append(cur.val)
            cur = cur.next
        cat = ""
        for value in valueList:
            cat+=str(value)

        cat = int(cat,2)
        return cat

