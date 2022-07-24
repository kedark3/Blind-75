class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # base case
        # if sum is odd, then we can't make two equal partitions in the array
        if len(nums) <= 1 or sum(nums) % 2:
            return False
        
        # take half-sum
        hsum = sum(nums) // 2
        
        # we need to see if using any of the element combinations in the array
        # if we can make hsum as the target
        # let's tart with a set of {0,nums[0]} as, at 0th index sum we can make is nums[0] or 0
        sum_set = set()
        sum_set.add(0)
        sum_set.add(nums[0])
        
        for i in range(1,len(nums)):
            dp = set()
            for v in sum_set:
                if v + nums[i] == hsum:
                    print(sum_set)
                    return True
                dp.add(v+nums[i])
                dp.add(v)
            sum_set = dp
        return True if hsum in sum_set else False
        