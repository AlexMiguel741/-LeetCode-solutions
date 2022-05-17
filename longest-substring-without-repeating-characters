# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        
        storage=""
        longest=0
        
        for character in s:
            if character in storage:
                longest=max(len(storage),longest)
                storage=storage[storage.index(character)+1:]

            storage+=character
            
        return max(longest,len(storage))
