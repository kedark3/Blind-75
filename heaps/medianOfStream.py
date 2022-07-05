import heapq as hq
class MedianFinder:

    def __init__(self):
        # we maintain two heaps, and ensure they are always almost equal sized, max difference
        # in size should be 1 or less
        self.minheap = []  # this stores all big values
        self.maxheap = []  # this stores all small values
        

    def addNum(self, num: int) -> None: # O(log n)
        hq.heappush(self.maxheap, -1 * num)  # O(log n) operation
        
        # make sure every num in maxheap is <= every num in min heap
        if (self.maxheap and self.minheap and (-1 * self.maxheap[0]) > self.minheap[0]):
            val = -1 * hq.heappop(self.maxheap) # O(log n) operation
            hq.heappush(self.minheap, val) # O(log n) operation

        # uneven size heaps - balance it
        # we always want both heaps to be almost same size or differ by 1 atmost
        # this way when we want the median, if both heaps are equal size, we can take 1 element
        # from each min and max heap such that minheap[0] + maxheap[0] / 2
        # if minheap or max heap is larger, then we just return the heap top as result from the longer one
        # e.g. if our heaps are [1,2] and [3,4] = minheap top will be 3 and max heap top will be 2, (3+2)/2 is our result
        # else if we have [1,2,3] [4,5] then maxheap top 3 is our result
        # else if we have [1,2] [3,4,5] then minheap top 3 is our result
        # hence we do pop the larger heap and push that value to smaller heap
        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1 * hq.heappop(self.maxheap) # O(log n) operation
            hq.heappush(self.minheap, val) # O(log n) operation
        
        if len(self.minheap) > len(self.maxheap) + 1:
            val =  hq.heappop(self.minheap) # O(log n) operation
            hq.heappush(self.maxheap, -1 * val) # O(log n) operation
            
            
    def findMedian(self) -> float: # O(1)
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]  # O(1)
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0] # O(1)
        return (-1 * self.maxheap[0] + self.minheap[0]) / 2 # O(1)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()