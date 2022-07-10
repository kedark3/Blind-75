# TC O(nlogn) as we are sorting start and end times
# SC O(n) as we create 2 new arrays of size n
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # base case - check actual input data        
        if not intervals:
            return 0
        # logic
        # Take 2 arrays- one for start times and one for end times
        # sort them both
        start_times = sorted([i for i,_ in intervals])
        end_times =  sorted([i for _,i in intervals])

        # start pointers at 0th index
        s_ptr = e_ptr = 0
        rooms = 0
        # iterate while both pointers are within the bounds
        while s_ptr < len(start_times) and e_ptr < len(end_times):
            # if at any point, s_ptr is pointing to time that is smaller than
            # current end_ptr that means new meeting needs to be started in a new room
            # while there is a previous mtg not yet ended at end ptr
            if start_times[s_ptr] < end_times[e_ptr]:
                rooms += 1
            else: # if values at start and end pointer are both same or start pointer is pointing to higher value
                # that means a meeting already ended and new meeting can be started in the same room
                # so no need to create 1 new room, just move end pointer to next location
                e_ptr += 1
            # in either cases start pointer keeps moving forward
            s_ptr += 1
        return rooms
    
        """
        e.g.
        
        input = [[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]
        start_times =[1, 2, 3, 8, 10, 11] 
        end_times = [7, 10, 12, 19, 20, 30]
        
        when algorithm starts, both pointers will be at 0th index
        s_ptr  e_ptr  rooms
        1       7       1
        2       7       2
        3       7       3
        8       7       3  --> # here we didn't increase room count as s_ptr is at 8 and e_ptr was at 7,
                            so that mtg would end and mtg that started at 8 will re-use that room.
        10      10      3 -->    same as above, e_ptr was at 10 and s_ptr also moved to 10. overlap is fine, no new room needed
        11      12      4 -->  we need new room here as previous mtg will keep going till 12, but curr mtg starts at 11
        
        At the end, s_ptr is out of bounds. we don't care to traverse the end _ptr 
        just return the result

        """
                


# TC O(nlogn) as we are sorting start and end times and also min heap takes LogN operations for each of up-to N elements we add to it
# SC O(n) as we create a heap of up to size N

import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # base case - check actual input data
        
        rooms  = []
        
        if not intervals:
            return 0
    
        intervals.sort()
        
        hq.heappush(rooms, intervals[0][1])  # push end time of the first meeting
        
        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                hq.heappop(rooms)
            
            hq.heappush(rooms, i[1])
        
        return len(rooms)