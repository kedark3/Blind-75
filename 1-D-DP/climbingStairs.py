class Solution:
    def climbStairs(self, n: int) -> int:
        # we need to find ways to get from 0th index to nth index
        # we can use bottom up DP to solve this. Way to get to `n`th location from `n`
        # is only 1, and from n-1->n is also only 1, but from n-2 onward till 0, we have 2 choices:
        # we can either take 1 jump or 2 jumps, so for any index in range(n-2,0,-1) we will do 
        # dp[i] = dp[i+1] + dp[i+2]
        # and at index 0 we will have our answer
        
        dp = [0] * (n+1)
        dp[n], dp[n-1] = 1,1
        
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]