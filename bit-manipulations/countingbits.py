class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0. 0  0000
        1. 1  0001
        2  1  0010
        3. 2  0011
        4. 1  0100
        5  2  0101
        6  2  0110
        7. 3  0111
        8. 1  1000
        
        
        """
        dp = [0,1]
        
        if n == 0: return dp[:1]
        if n == 1: return dp
        
        offset = 2
        for i in range(2,n+1):
            if i == 2 ** dp[i-1] :
                offset = i
            dp.append(1 + dp[i - offset])
        
        return dp