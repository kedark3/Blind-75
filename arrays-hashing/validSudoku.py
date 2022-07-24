# TC: O(9^2)
# SC: O(9^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        # key will be tuple of (r//3,c//3) for squares
        squares = collections.defaultdict(set) 
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in squares[(i//3,j//3)]):  
                    # for every index pair i,j- if we do i//3 and j//3
                    # it gives us a number in 0,1,2 and that helps us
                    # identify correct square
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])

        return True