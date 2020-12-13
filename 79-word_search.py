class Solution(object):
    def exist(self, board, word):
        self.found = False
        self.word = word
        self.visitedSet = set()
        for row in range(len(board)):
            for col in range (len(board[0])):
                self.search(board,row,col,0)
                if self.found:
                    return True
        return False
        
        
    def search(self,board,row,col,index):
        if index==len(self.word):
            self.found = True
        
        if not self.found and row>=0 and col>=0 and row<len(board) and col<len(board[0]) and (row,col) not in self.visitedSet and board[row][col]==self.word[index]:
            self.visitedSet.add((row,col)) 
                              
            self.search(board,row,col+1,index+1)
            self.search(board,row,col-1,index+1)            
            self.search(board,row+1,col,index+1)            
            self.search(board,row-1,col,index+1)              
                              
            if not self.found:
                self.visitedSet.remove((row,col))