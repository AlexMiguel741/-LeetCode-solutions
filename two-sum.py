# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storage={}
        
        
        for idx, value in enumerate(nums):
            
            diff=target-value
            
            if diff in storage:
                return [storage[diff],idx]
            else:
                storage[value]=idx
                
        return []
