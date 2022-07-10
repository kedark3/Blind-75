# TC O(n) as we iterate only once
# SC O(n) as we store dp array, if we eliminate dp array then we can do constant time
class Solution:

    def numDecodings(self, s: str) -> int:
        # use dp approach
        # Bottom up DP - for each element starting at last index down to first
        # if index i + index i+1 is within 26 then dp[i] = dp[i+1]+dp[i+2] else its just dp[i+1]
        # if there is a 0 anywhere, it should be prefixed by 1,2 else it can't be decoded
        # hence a valid string will have 0 only prefixed with 1 or 2 anywhere in the string
        
        # base cases
        n = len(s)
        if s[0] == "0" or s[-1] == "0" and s[-2] not in "12" or not s:
            return 0
        if n == 1:
            return 1

        # logic
        # take dp array of size n+1 so we can mark base case n+1 as 1 at the last index
        dp = [0] * (n+1)
        # as we already checked last element is not "0" we can safely say we can decode 
        # last element in 1 way
        dp[-1] = 1
        # reverse loop
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if (i+1) < n and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]


# TC O(n) as we iterate only once
# SC O(1) as we eliminate the DP array

class Solution:

    def numDecodings(self, s: str) -> int:
        # use dp approach
        # Bottom up DP - for each element starting at last index down to first
        # if index i + index i+1 is within 26 then dp[i] = dp[i+1]+dp[i+2] else its just dp[i+1]
        # if there is a 0 anywhere, it should be prefixed by 1,2 else it can't be decoded
        # hence a valid string will have 0 only prefixed with 1 or 2 anywhere in the string
        
        # base cases
        n = len(s)
        if s[0] == "0" or s[-1] == "0" and s[-2] not in "12" or not s:
            return 0
        if n == 1:
            return 1

        # logic
        
        dpi2 = 1
        dpi1 = 1
        # reverse loop
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dpi = 0
            else:
                dpi = dpi1
            if (i+1) < n and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                dpi += dpi2
            dpi2 = dpi1
            dpi1 = dpi            
        return dpi

