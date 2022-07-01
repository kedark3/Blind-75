"""
https://leetcode.com/problems/maximum-frequency-stack/
Complexity Analysis

Time Complexity: O(1) for both push and pop operations.

Space Complexity: O(N), where N is the number of elements in the FreqStack. 
"""
class FreqStack:

    def __init__(self):
        # use this to counte frequencies of each element
        self.freq = collections.Counter()  # this is just a special dict with purpose of counting, doesn't throw keyerror
        # use this to store the elements in K:V format
        # where K is frequency and value is [list of elements with that freq]
        self.group = collections.defaultdict(list)  # doesn't throw keyError if something is missing, just returns Default value
        # used to keep track of max freq and when we have to pop we use this to look up
        # correct group number
        self.maxfreq = 0

    def push(self, x):
        # get the freq of x and add 1 to it
        f = self.freq[x] + 1
        # update the freq in freq counter dict
        self.freq[x] = f
        # if freq crossed our max freq, update the max freq
        if f > self.maxfreq:
            self.maxfreq = f
        # use the freq to append x to correct group
        self.group[f].append(x)

    def pop(self):
        # pop item from group where group no is == maxfreq
        x = self.group[self.maxfreq].pop()
        # reduce freq of the popped item by 1
        self.freq[x] -= 1
        # if group no longer has any elements at max freq, then reduce max freq by 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()