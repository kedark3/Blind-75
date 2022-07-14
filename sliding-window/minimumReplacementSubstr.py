# https://leetcode.com/problems/minimum-window-substring/
# Approach single hashmap approach and only one variable.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Approach: Use Sliding window
        # TC O(N)
        # SC O(1)
        
        # base case
        if len(t) > len(s): return ""
        
        # logic
        
        # declarations
        res = []
        res_len = float("Infinity")
        
        t_map = {}
        # create a t_map for frequency of characters
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        # set low to 0
        l = 0
        exp_match = len(t_map) # exp match count is len of t_map
        match = 0

        for i in range(len(s)):
            c = s[i]
            # if c in t_map we decrease count in t_map
            if c in t_map:
                t_map[c] -= 1
                # if count reaches 0, we increase match count
                if t_map[c] == 0:
                    match += 1
            # while match and exp_match are same we try to shrink window from left side
            # because we want to shrink window and find smallest window with all chars in c
            while match == exp_match:
                if res_len > (i - l + 1):
                    res = [l, i]
                    res_len = (i - l + 1)
                # if char at `l` is in t_map increase its count, and when count became 1
                # that means we no longer match the required counts and help break the loop
                if s[l] in t_map:
                    t_map[s[l]] += 1
                    if t_map[s[l]] == 1:
                        match -= 1
                # keep moving left pointer
                l += 1

        
        return s[res[0]:res[1]+1] if res_len != float("Infinity") else ""        

# approach 2 : with have and need and 2 hashmaps
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Approach: Use Sliding window
        # TC O(N)
        # SC O(1)
        
        # base case
        if len(t) > len(s): return ""
        
        # logic
        
        # declarations
        res = []
        res_len = float("Infinity")
        have, need = 0, 0
        window, tmap = {}, {}
        l = 0 # left pointer
        
        # freq map for string t
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        
        # gives us number of conditions we have to meet
        # if our tmap has {"a":3} that meets we only need to meet one condition
        # that would be need = 1
        need = len(tmap) 
        
        # iterate over s
        for r in range(len(s)):
            # take the current character
            c = s[r]
            # add each character to the window
            window[c] = window.get(c, 0) + 1

            # check if char is in the tmap and it matches the count we need
            if c in tmap and window[c] == tmap[c]:   
                have += 1   # if we did, increment the count
            
            # while condition was met update the result and shrink the window
            while have == need:
                # if current window is smaller than previous res_len
                if (r - l + 1) < res_len: # update the result
                    res = [l,r]
                    res_len = (r - l + 1)
                    
                # move left pointer and
                # drop its count
                window[s[l]] -= 1
                # if count required is no longer met, we reduce have by 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if res_len != float("Infinity") else ""        