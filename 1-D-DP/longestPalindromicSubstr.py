# O(N^2) solution as len of string is N and expanding palindrome around center can take upto N times moving l,r pointers in worst case
# SC O(N) : As we keep re-using result variable to store the result, its max len is N but one can argue result is not counted. so O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base
        # if string just has 1 element
        if len(s) == 1:
            return s
        # let's ensure string is longer than 2 elements
        if len(s) == 2 and s[0] == s[1]:
            return s
        
        
        # logic
        res = []
        # for each letter in the string, start expanding window using 2 pointers
        for i in range(len(s)):
            l, r = i, i  # try odd len palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1] if len(s[l:r+1]) > len(res) else res
                l -=1
                r +=1
                
            l, r = i, i+1  # try even len palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1] if len(s[l:r+1]) > len(res) else res
                l -=1
                r +=1
                
        
        return ''.join(res)
            