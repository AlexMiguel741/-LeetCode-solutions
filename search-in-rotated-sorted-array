# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #try to find the pivot point
        n=len(nums)
        
        pivot=0
        for i in range(0,n-1):
            if nums[i+1]<nums[i]:
                pivot=i
                break
        
        #print(nums[0:pivot+1])
        #print(nums[pivot+1:])
        
        val1=self.binary_search(nums[0:pivot+1],target)
        
        if val1==-1:
            val2=self.binary_search(nums[pivot+1:],target)
            if val2!=-1:
                return val2+len(nums[0:pivot+1])
            else:
                return val2
        else:
            return val1
        
    
    def binary_search(self, nums,t):
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]<t:
                l=m+1
            elif nums[m]>t:
                r=m-1
            else:
                return m
        return -1
