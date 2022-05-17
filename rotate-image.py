# https://leetcode.com/problems/rotate-image/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #up and down 
        matrix.reverse()
        temp=0
        dim=len(matrix[0])
        for i in range(dim):
            for j in range(dim):
                if j>i:#inverti i valori della digonale superiore
                    temp=matrix[j][i]
                    matrix[j][i]=matrix[i][j]
                    matrix[i][j]=temp
