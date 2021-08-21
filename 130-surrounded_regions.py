# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        width, height = len(board[0]), len(board)
        queue = collections.deque()
        for i in range(width):
            if board[0][i] == 'O':
                queue.append((0, i))
            if board[height-1][i] == 'O':
                queue.append((height-1, i))
        for j in range(1, height-1):
            if board[j][0] == 'O':
                queue.append((j, 0))
            if board[j][width-1] == 'O':
                queue.append((j, width-1))

        while queue:
            i, j = queue.popleft()
            if 0 <= i < height and 0 <= j < width and board[i][j] == 'O':
                board[i][j] = 'N'
                queue.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

        for j in range(width):
            for i in range(height):
                board[i][j] = 'O' if  board[i][j] == 'N' else 'X'

'''
Time complexity: 
O(|V|+|E|) = O(b**d)
Space complexity: O(|V|+|E|) = O(b**d)
'''

# DFS
class Solution:
    def solve(self, board):
        width, height = len(board[0]), len(board)
        for i in range(width):
            if board[0][i] == 'O':
                self.search(board, 0, i)
            if board[height-1][i] == 'O':                
                self.search(board, height-1, i)
        for j in range(1, height-1):
            if board[j][0] == 'O':
                self.search(board, j, 0)
            if board[j][width-1] == 'O':
                self.search(board, j, width-1)

        for j in range(width):
            for i in range(height):
                board[i][j] = 'O' if  board[i][j] == 'N' else 'X'

    def search(self, board, i, j):
        width, height = len(board[0]), len(board)
        if 0 <= i < height and 0 <= j < width:
            if board[i][j] == 'O':
                board[i][j] = 'N'
                self.search(board, i-1, j)
                self.search(board, i+1, j)
                self.search(board, i, j-1)
                self.search(board, i, j+1)

'''
Time complexity:
O(|V|+|E|) with |V| the number of vertex, |E| the number of edges
= O(b**d) with b the branching factor and d the depth

Space complexity:
O(|V|)
= O(bd)
'''