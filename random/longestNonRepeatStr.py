# Linear TC and Linear SC.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Function takes a string as input and provides longest substring len as output
        Args: s: str
        Returns: int: len of longest substr
        """

        # base condition
        if not isinstance(s,str) or len(s) == 0:
            return 0

        # quick len check
        if len(set(s)) == len(s):  # e.g. "abc" -> set() -> {'a','b','c'} 
            return len(s)

        # core logic
        result = 0
        mp = {}
        i = 0
        
        for j in range(len(s)):
            print(i,j,mp, s[j])
            # if the char is in the map
            if s[j] in mp:
                # then increment i to the point where it crosses the location of that character in the string
                i = max(mp[s[j]],i)
            # at every step calculate diff between j-i +1(to compensate for base 0 of lists) & do max of that with result
            result = max(result, j-i+1)
            # this is where we saw the character last time, we keep incrementing that for each character
            mp[s[j]] = j + 1
        
        return result   