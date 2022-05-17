# https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        
        
        rows_founded=set()
        cols_founded=set()
        
        for i in range(n):
            for j in range(m):
                
                if matrix[i][j]==0:
                    rows_founded.add(i)
                    cols_founded.add(j)
                    
                    
                    
        for i in range(n):
            for j in range(m):
                if i in rows_founded:
                    matrix[i][j]=0
                if j in cols_founded:
                    matrix[i][j]=0
            
        
        
              
        return matrix
