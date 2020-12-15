#Transpose and then reverse = Rotation
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        #transpose matrix and reverse each row
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            #reverse each row
            matrix[i].reverse()

'''
Time complexity: O(n^2)
Space complexity: O(1) in place rotation
'''

#Approch 2: Rotate four rectangles in one single loop
#I recommend writting down an example in order to derive the 4 permutations
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
'''
same complexities
'''
