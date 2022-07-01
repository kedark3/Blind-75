# DP TC O(N), SC O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cMax, cMin = 1, 1
        res = max(nums)
        
        for n in nums:
            t = cMax * n  # store this value so can be used in cMin calculation
            cMax = max(cMax * n, cMin * n, n)
            cMin = min(t, cMin * n, n)
            res = max(res, cMax, cMin)
        return res