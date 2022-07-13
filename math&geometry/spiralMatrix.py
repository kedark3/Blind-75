class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left, right, bottom = 0, 0, len(matrix[0])-1, len(matrix)-1
        result = []
        
        while top <= bottom and left <= right:
            
            #  top row
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            # right column
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            # bottom row
            if top <= bottom:
                for i in range(right,left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            # left column
            if left<= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            # continue for inner matrix
        return result