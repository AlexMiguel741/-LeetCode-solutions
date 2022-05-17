# https://leetcode.com/problems/group-anagrams/
class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result={}
        n=len(strs)
        for i in range(0,n):
            stringa=strs[i]
            sorted_string="".join(sorted(stringa))
            
            if sorted_string not in result:
                result[sorted_string]=[stringa]
            else:
                result[sorted_string].append(stringa)   
            
        return [i for i in result.values()]
