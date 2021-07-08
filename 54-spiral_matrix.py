# Approach 1: easy to understand by space complexity is high
class Solution:
    def spiralOrder(self, matrix):
        width, height = len(matrix[0]), len(matrix)
        
        res = []
        xmin, xmax = 0, width-1
        ymin, ymax = 0, height-1

        columns = list(zip(*matrix))
        while ymin <= ymax and xmin <= xmax:
            res += matrix[ymin][xmin:xmax+1]
            res += columns[xmax][ymin+1:ymax+1]
            if ymin < ymax and xmin < xmax:
                res += matrix[ymax][xmin:xmax][::-1]
                res += columns[xmin][ymin+1:ymax][::-1]

            ymin += 1
            ymax -= 1
            xmin += 1
            xmax -= 1

        return res

# Approach 2: Using a generator (we could also have incorporated the generator in the while loop)
class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

'''
Time Complexity: O(N)O(N), where NN is the total number of elements in the input matrix. We add every element in the matrix to our final answer.

Space Complexity:

O(1)O(1) without considering the output array, since we don't use any additional data structures for our computations.

O(N)O(N) if the output array is taken into account.
'''