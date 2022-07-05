class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s = set()
        # for n in nums:
        #     if n in s:
        #         return True
        #     s.add(n)
        # return False
        if len(nums) < 2:
            return False
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
            