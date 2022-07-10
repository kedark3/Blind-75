class Solution:
    dirs = {(1,0),(-1,0),(0,1),(0,-1)}  # D, U, R, L directions
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0:
            return False
        if not word or len(word) == 0:
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]: # when we find first char of wrod in matrix
                    # call DFS on it
                    if self.dfs(board, word, i, j, 0): # if it returns True, terminate program
                        return True
                    # else continue
        return False  # if we didn't return True so far means word is missing. So False.
                    
    
    def dfs(self,board, word, i, j, index):
        if index == len(word):
            # when index become same as word len means that our word is already found
            # indices are 0 based remember?
            return True
        if i < 0 or i >= len(board) or j<0 or j>=len(board[0]) or board[i][j]=="#":
            # if going out of bounds or found a visited node, its not valid path, return False
            return False
        
        if board[i][j] == word[index]:
            for dr,dc in self.dirs:  # for all directions
                # calculate new indices
                nr = i + dr
                nc = j + dc
                
                # action - Mark char as visited by replacing it with a #
                board[i][j] = "#"   # mark it as visited
                #recurse - pass nr,nc and new index = index+1
                if self.dfs(board,word, nr,nc, index+1):
                    # if this returned True, we don't care to backtrack and reverse our action anymore
                    # we will leave matrix in modified state and return
                    return True
                
                # backtrack - If we arrived here means, we couldn't find what we were looking for
                # so mark it unvisited so it can be explored from other directions
                board[i][j] = word[index]
        # if we made it here means we didn't find our word, so False.
        return False
                
        