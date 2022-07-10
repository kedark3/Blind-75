class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        for start,end in intervals:
            if start > newInterval[1]:
                # if new interval starts after current `newInterval` ends, then
                # append newInterval to res
                # and return res +rest of the intervals
                # this also handles the case where new Interval is [0,0] or starts before
                # 1st interval in intervals list. So we just add that in the beginning and 
                # return the result
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                # if current interval end before new interval starts
                # add that to result as is
                res.append([start,end])
            else:
                # if neither of above is true, that means we have an overlapping interval
                # merge those two, but don't add it to result just yet, what if there are more
                # intervals overlapping with this updated newInterval. We will keep merging all before
                # inserting it in the list
                newInterval = [min(start,newInterval[0]), max(end,newInterval[1])]
                
            i += 1 # using `i` to keep track of where we are since we are not looping using i and we need i on line 14
        # if we came out of the loop, then we didn't ever add the newInterval anywhere
        # so add it to the end. This is edge case where new Interval starts after all other intervals end
        res.append(newInterval) 
        return res