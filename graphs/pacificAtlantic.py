# TC: O(m*n) - we are only visiting nodes 1 time
# SC: O(m*n)- at most in our visited sets we will have m*n elements of 2 tuples so 2*m*n And recursion stack space m*n
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            # base
            # check bounds
            if r < 0 or r == ROW or c < 0 or c == COL or (r,c) in visited or heights[r][c] < prevHeight:
                return
            
            # logic
            visited.add((r,c))
            # visit 4 directions
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL-1])
        
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, atl, heights[ROW-1][c])
            
        return atl & pac



# Approach 2: BFS

from collections import deque as dq
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()
        pq, aq  = dq(), dq()
        dirs = {(1,0), (-1,0), (0,1), (0,-1)}
        
        for r in range(ROW):
            pq.append((r,0))
            aq.append((r, COL-1))
        
        for c in range(COL):
            pq.append((0, c))
            aq.append((ROW-1, c))
        
        # process pacific
        while pq:
            r,c = pq.popleft()
            pac.add((r,c))
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < ROW and nc >= 0 and nc < COL and (nr,nc) not in pac and heights[nr][nc] >= heights[r][c]:
                    pq.append((nr,nc))
            
            
            
        # process atlantic
        while aq:
            r,c = aq.popleft()
            atl.add((r,c))
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < ROW and nc >= 0 and nc < COL and (nr,nc) not in atl and heights[nr][nc] >= heights[r][c]:
                    aq.append((nr,nc))
            
        # set intersection
        return atl & pac