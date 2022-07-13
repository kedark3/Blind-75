class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP Approach
        # TC : O (M*N)
        # SC : O(N) as we create 1 row initially and 1 in each loop that we recycle
        # as the entire bottom row is just 1s
        # and we don't need entire matrix, we just need one row
        # that we can keep recycling
        dp_row = [1] * n
        
        for i in range(m - 1):
            # for m - 1 rows, i.e. if m = 3, except last row
            # all other rows, we need to compute. last row is all 1s
            # create new row for each computation
            new_row = [1] * n # initially we will have all 1s
            for j in range(n - 2, -1, -1): # use n-2 as right column is also always 1
                # but then overwrite it with addition of value on the right and below
                new_row[j] = new_row[j + 1] + dp_row[j]
            # and overwrite previous dp_row with new_row
            dp_row = new_row
        return dp_row[0]
        


