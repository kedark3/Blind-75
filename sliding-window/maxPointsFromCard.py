# Approach : Sliding window
# TC : O(n)
# SC : O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)

        # we take sum of last k elements and make it curr/max sum
        max_sum = curr_sum = sum(cardPoints[-k:])
        # we form a window starting at 1st index till n-kth index
        l, r = 1, len(cardPoints) - k
        # in a loop, we keep adding l-1 th element to sum and remove current 
        # right most element from the sum that maintains curr_sum equal to `k` 
        # elements outside of the window
        while r < len(cardPoints):
            curr_sum = curr_sum - cardPoints[r] + cardPoints[l-1]
            max_sum = max(max_sum, curr_sum)
            l += 1
            r += 1
        return max_sum
            
        