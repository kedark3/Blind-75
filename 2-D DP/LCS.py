"""
Approach1: Use recursion with memoization(lru_cache)
Algortihm would look something like this:
Recursively traverse both strings, if either of those are empty then
in that case return 0 as the base case
else: 
take the first letter(l1) from txt 1 and find its first occurence in txt2. If
it is part of the optimal solution, then next recursive call would be 
1+ lcs(txt1[1:], txt2[l1+1:]) and if not then it will be lcs(txt1[1:],txt2)
but the first recursive call will only happen if the l1 is part of t2, else skip 
making that recursive call
Finally return max of both options we explored.
TC O(M*N^2) there are M possile positions for firsrt string and N for second, that gives us M*N
Solving each subproblem requires O(N) operations searching for a char in string N. Hence altogether M*N^2
SC O(M*N) we need to store answer for each of the MN subproblems
"""
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)  # use lru_cache for memoization of function calls to avoid re-computation
        def LCS(p1,p2):  # pass p1 and p2 pointers instead of passing text and slicing it for each step
            if len(text1) == p1 or len(text2) == p2:
                return 0
            
            # find first occurence of char at p1 index in text1 in text2 on or after p2 because we don't want to
            # keep finding the character in the beginning over and over again
            idxOf = text2.find(text1[p1], p2)
            # if we didn't consider the first char even though it may appear in text2
            # then we just drop it from text1 and call LCS on rest of it and the entire text2 starting at p2
            case1 = LCS(p1+1, p2)
            case2 = 0
            if idxOf != -1:
                # if we are considering the char at p1, then move p1 + 1 and idxOf+1 to filter the substring before
                # the first occurance of the character
                case2 = 1 + LCS(p1+1, idxOf+1)
            
            return max(case1, case2)
        
        return LCS(0,0)

"""
Approach2: Use recursion with improved memoization(lru_cache)
Algortihm would look something like this:
If first char of both substrings is not the same, then either one or both
charas will not be used. Therefore ans will be max(LCS(p1+1,p2), LCS(p1,p2+1))

When both strings are having matching characters in the beginning, we can do
1+ LCS(p1+1,p2+1)

TC O(M*N) solving each subproblem costs O(1) and there are M*N subproblems
SC O(M*N) we are storing the answer for each subproblem in cache and using recursive stack
"""
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)  # use lru_cache for memoization of function calls to avoid re-computation
        def LCS(p1,p2):  # pass p1 and p2 pointers instead of passing text and slicing it for each step
            if len(text1) == p1 or len(text2) == p2:
                return 0
            
            case1 =  max(LCS(p1+1, p2),LCS(p1,p2+1))
            case2 =0
            if text1[p1] == text2[p2]:
                case2 = 1 + LCS(p1+1, p2+1)
        
            return max(case1, case2)
        
        return LCS(0,0)


"""
Approach3: DP
Consider following example:
   a  c  d  e
a  X            0
b     X         0
c     X         0
d        X      0
e           X   0
f           X   0
   0  0  0  0   0
   
X's show that the path we will need to take to find the LCS. X moves down if we don't find a match
in curr row and col, and if we do, we make X move diagonally right in next row.

To compute the value of X, we can do a bottom up DP:
1) Initialize DP matrix of 0s of size rows=len(text1)+1 and cols=len(text2)+1
2) Traverse DP matrix in reverse order from len(text1)-1 and len(text2)-1 
3) At each step, see if chars are matching, is so then DP[i][j] = 1+dp[i+1][j+1]
4) If they don't match, DP[i][j] = max(DP[i][j+1], DP[i+1][j]) i.e. from next col in same row and same col in next row
Return DP[0][0]

TC O(M*N) for going over the DP matrix once
SC O(M*N) for matrix
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        return dp[0][0]

