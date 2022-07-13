class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, h = 0, 0
        res = 0
        hmap = {}
        
        while h < len(s):
            # add char to hashmap
            hmap[s[h]] = hmap.get(s[h],0) + 1
            # window size
            wsize = h - l + 1
            # get max freq
            max_f = max(hmap.values())
            
            # logic 
            # while we are meeting the condition, keep improving result
            if wsize - max_f <= k:
                res = max(res, wsize)
            else:# when we don't meet condition, decrement char at low pointer in hmap and move low+=1
                hmap[s[l]] = hmap.get(s[l],0) - 1
                l += 1
            # high pointer should always move because even if we moved low pointer
            # that will only reduce window size and won't yield better result than what we already had
            # so no point in keeping high pointer at the same location
            h += 1
            
        return res