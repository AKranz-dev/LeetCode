class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        box = head
        valueList = []
        reverseList = []
  

        while box is not None:
            valueList.append(box.val)
            box = box.next
        
        for num in valueList:
            reverseList.append(num)
        
      
         
        reverseList.reverse()
        
        for rnum, vnum in zip(reverseList, valueList):
            if  rnum != vnum:
                return False
        return True
