# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        to_scan=list(s)
        stack=[]
        
        for i in range(len(to_scan)):
            
            if to_scan[i]=='(':
                stack.append(i)
            elif to_scan[i]==')':
                if stack:
                    stack.pop()
                else:
                    to_scan[i]=''
                     
        for i in stack:
            to_scan[i]=''
            
                
        return "".join(to_scan)
