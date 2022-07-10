class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # base
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: x[0]) # O(nlogn)
        # [[1,2], [2,3],[2,4],[3,4]]
        # logic
        ans = 0
        i = 1
        prevEnd = intervals[0][1] 
        
        for start,end in intervals[1:]: # O(n)
            if start >= prevEnd:
                prevEnd = end
            else:
                ans += 1
                prevEnd = min(prevEnd, end)
        return ans