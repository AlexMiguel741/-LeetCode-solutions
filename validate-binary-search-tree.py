# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        visited=self.in_order_traversal(root)
        
        for i  in range( len(visited)-1):
            if visited[i+1]<=visited[i]:
                return False
        else:
            return True
            
        
    def in_order_traversal(self, root):
        el=[]
        
        if root.left:
            el+=self.in_order_traversal(root.left)
        
        el.append(root.val)
        
        if root.right:
            el+=self.in_order_traversal(root.right)
        
        return el
