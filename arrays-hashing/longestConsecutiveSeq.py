class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach 1 : sort the arr - but that will be O(nlogn) solution
        # Approach 2: Use memory to trade off for better speed O(n)
        
        # Create a set of nums
        s = set(nums)
        longest = 0 # longest consecutive seq so far is 0
        for n in nums:
            if n - 1 not in s: # means n doesn't have a left neighbor, so it can be beginning of a set
                length = 1 # set length to 1
                while n + length in s: # iterate over set until we keep finding n+length in the set
                    length += 1  # if we did, increase it by 1
                longest = max(length, longest) # if we exited while loop, ensure to update longest
        return longest