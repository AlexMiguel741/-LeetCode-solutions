# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        if head is None:
            return
        next=None
        prec=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prec
            prec=curr
            curr=nxt
        return prec
