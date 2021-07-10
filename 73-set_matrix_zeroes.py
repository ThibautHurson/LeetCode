# Approach 1: 
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        nb_rows, nb_col = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(nb_rows):
            for j in range(nb_col):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(nb_rows):
            for j in range(nb_col):
                if i in rows or j in cols:
                    matrix[i][j] = 0
'''
Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.

Space Complexity: O(M+N).
'''


# Approach 2: Space efficient 
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        nb_rows, nb_col = len(matrix), len(matrix[0])
        is_col = False
        for i in range(nb_rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, nb_col):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
                    
        for i in range(1, nb_rows):
            for j in range(1, nb_col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, nb_col):
                matrix[0][j] = 0
        if is_col:
            for i in range(nb_rows):
                matrix[i][0] = 0

'''
The idea is that we can use the first cell of every row and column as a flag. This flag would determine 
whether a row or column has been set to zero. This means for every cell instead of going to M+NM+N cells 
and setting it to zero we just set the flag in two cells.
Time Complexity : O(M×N)
Space Complexity : O(1)
'''

mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
print(sol.setZeroes(mat))
