# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False
        curr=head
        vals=[]
        while(curr):
            vals.append(curr.val)
            curr=curr.next
        
        return vals==vals[::-1]
