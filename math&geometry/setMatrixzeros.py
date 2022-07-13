# with no additional space. # TC O(mn) SC O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        rzero, czero = [0] * ROWS, [0] * COLS
        
        # add all locations where we have zeros to rzero and czero        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rzero[i] = 1
                    czero[j] = 1

        # update rows with zeros
        for i in range(ROWS):
            if rzero[i] == 1:
                for j in range(COLS):
                    matrix[i][j] = 0
                
        # update cols with zeros
        for i in range(COLS):
            if czero[i] == 1:
                for j in range(ROWS):
                    matrix[j][i] = 0


# with no additional space. # TC O(mn) SC O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False # set this to true if we need to make 0th row zero
        
        # add all locations where we have zeros to rzero and czero        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # update rows with zeros
        for i in range(1,ROWS):
            if matrix[i][0] == 0:
                for j in range(COLS):
                    matrix[i][j] = 0
                
        # update cols with zeros
        for i in range(COLS):
            if matrix[0][i] == 0:
                for j in range(ROWS):
                    matrix[j][i] = 0
        
        if rowZero:
            for j in range(COLS):
                    matrix[0][j] = 0


