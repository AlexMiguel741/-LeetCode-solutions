# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        
        stored=set()
        
        n=len(nums)
        
        nums.sort()
        
        for i in range(n-2):
            
            left=i+1
            right=n-1
            
            while(left<right):
                
                if (nums[left]+nums[right]+nums[i])<0:
                    left=left+1
                elif (nums[left]+nums[right]+nums[i])>0:
                    right=right-1
                else:
                    stored.add( (nums[left],nums[right],nums[i]))
                    left=left+1
                    right=right-1
        
        return list(stored)
