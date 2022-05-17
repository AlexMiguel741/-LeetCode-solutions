# https://leetcode.com/problems/majority-element/
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==0:
            return 
        
        majority=len(nums)/2
        
        frequency={}
        
        for i in nums:
            if i not in frequency:
                frequency[i]=1
            else:
                frequency[i]+=1
        
        for key in frequency:
            if frequency[key]>majority:
                return key
