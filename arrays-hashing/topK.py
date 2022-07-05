class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use bucket sort
        count = {} # count list for counting freq of each element in nums
        freq = [[] for i in range(len(nums)+1)]  # empty list for each element index in len(nums)+1
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n) # append num to freq[c] list
        
        res = []
        for i in range(len(freq)-1, 0, -1):# for each item in freq list
            for val in freq[i]: # for each value in that list
                res.append(val) # append to result
                if len(res) == k:  # when res == k = return res
                    return res

