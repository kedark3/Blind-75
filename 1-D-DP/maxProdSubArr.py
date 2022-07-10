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


"""
Approach - at each step calculate what's the max and min we can make there
e.g. 
            2      3      -2      4
max/min     2/2    6/6    -2/-12  4/-48 

Result is max of whatever min/max we found. so 6 in this case.
"""