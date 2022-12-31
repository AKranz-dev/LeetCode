#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        headLength = len(head)
        i=0
        for number in head:
            print("The first number is {} and the checking number is {}".format(number, head[headLength-head.index(number)-1]))
            if number == head[headLength-head.index(number)-1]:
                i+=1
            else:
                return False
        if i==headLength:
            return True

mySolution = Solution()
#head = [1,2]
head = [1,2,2,1]
head = [1,5,32,45,5,3,5,5,3,3,5,6,76,4,3,32,2,2,32,3,4,76,6,5,3,3,5,5,3,5,45,32,5,1]
print(mySolution.isPalindrome(head))