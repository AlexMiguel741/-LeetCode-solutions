# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        storage={}
        A=set(nums1)
        B=set(nums2)
        
        for i in A:
            if i not in storage:
                storage[i]=1
            else:
                storage[i]+=1
        
        for i in B:
            if i not in storage:
                storage[i]=1
            else:
                storage[i]+=1
        
        result=[]
        
        for idx in storage:
            if storage[idx]>1:
                result.append(idx)
        
        
        return result
