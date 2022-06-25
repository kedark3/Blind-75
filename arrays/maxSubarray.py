class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        if len(nums) == 1:
            return nums[0]
        currS = maxS = nums[0]
        
        for i in range(1,len(nums)):
            currS = max(currS + nums[i], nums[i])
            maxS = max(maxS, currS)
        return maxS