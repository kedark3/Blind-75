class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # this is same code as house robber 1
        def robber(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                tmp = max(n+rob1, rob2)  # for each house, we choose curr+n-2(i.e. n+ rob1) else n-1 (i.e. n-1), store that in tmp and update those below
                rob1 = rob2
                rob2 = tmp
            
            return rob2
        # only difference is, as the house 0 and house n-1 are next to each other, we can't rob them both
        # to avoid that, we run house robber 2 times, on nums[1:] and nums[:-1], excluding 1st and last house respectively
        # thought process:
        # When we rob house 1, we eliminate house n-1 automatically, so calculate values based on 1->n-1 houses
        # then we skip house 1, we can rob n-1th house as well, so calculate 2->n max value
        # whatever is max out of two is what we should get after the robbery
        return max(robber(nums[1:]), robber(nums[:-1]))