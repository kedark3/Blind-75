class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        
        if len(intervals) == 0: # if there are no mtgs, you can assume you attended everything
            return True # hence True
        
        for i in range(1,len(intervals)): # start at index 1 as index 0 can be assumed that we can always attend
            if intervals[i][0] < intervals[i-1][1]: # curr mtg starts before last one ends
                return False
        return True
        