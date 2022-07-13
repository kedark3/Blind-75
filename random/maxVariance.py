from collections import defaultdict

class Solution:
    def largestVariance(self, s: str) -> int:
        char_set = set(s)
        result = 0
        d = defaultdict(list)
        for i,char in enumerate(s):
            # we need this map because if we have more than 2 characters in the string
            # we want to use this map in the loop below to merge occurences of set of 2 characters 
            # at a time and sort them according to their index in the resulting list
            d[char].append((i,char)) 

        # we restrict the loops to character set, instead of all 26 characters in the english lowercase
        # it's sort of optimization
        for c1 in char_set:
            for c2 in char_set:
                # two loops means we take pair of characters at a time.
                # so in our exampe string "aababbb" it will do "a,b" then "b,a"
                if c1 != c2:
                    # but we need to check they are not equal because we are using sets we 
                    # may run into issue where both chars are equal, sets are unordered
                    # we only want to run algorithm on the pair of distinct characters
                    
                    # we initialize currVariance and lastDiff to 0
                    currVar, lastDiff = 0, 0
                    # minDiff to infinity
                    minDiff = float("Infinity")
                    # then we created sorted list of `c1` and `c2` frequencies
                    for _, c in sorted(d[c1]+d[c2]):
                        # print(minDiff)
                        # for every char matching c1, increase var by 1
                        if c == c1:
                            currVar += 1
                        elif c == c2:
                            # and if it matches c2 decrease var by 1
                            currVar -= 1
                            # when we do so, ensure to update minDiff
                            minDiff = min(minDiff,lastDiff)
                            # and lastly lastDiff
                            lastDiff = currVar
                        # result at each step will be max of result and diff in (currVar - minDiff)
                        result = max(result, currVar - minDiff)
                        
        return result