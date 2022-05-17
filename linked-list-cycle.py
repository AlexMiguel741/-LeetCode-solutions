# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        
        curr=head
        while(curr):
            
            if str(curr.val)=='T':
                return True
            
            curr.val='T'
            curr=curr.next
            
        return False
