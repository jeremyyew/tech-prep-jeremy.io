'''
- We can traverse the matrix directly using DFS. The tricky part is marking where we've recently traversed, since we cant re-use cells.
- We can't simply overwrite the entire board at the beginning of each new search, since everytime we backtrack and continue searching from an intermediate cell we need to keep the prefix series of cells marked. 
- So we use the callstack. Once we've traversed all paths that lead from the current cell and did not find any correct paths, the current cell will not be used at the current position of the word. 
- So we rewrite its old value (free-ing it for re-use) and then backtrack. 

'''

def exist(self, board, word):
    if not board:
        return False
    w = len(board)
    h = len(board[0])
    
    def dfs(self, board, i, j, word):
        if len(word) == 0: 
            return True
        if not (0 <= i <= w) or not (0 <= j <= h) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  
        board[i][j] = "#" 
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
    
    for i in range(w):
        for j in range(h):
            if dfs(board, i, j, word):
                return True
    return False
 
