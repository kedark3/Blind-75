class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() # n log n
        
        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        for i in range(len(nums)):
            if (i+1) < len(nums) and nums[i] + 1 != nums[i+1]:
                return nums[i]+1
        return i+1
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Bit manipulation:
        # if we XOR (^) a number with itself, it yields 0
        # if we initialize missing number to len(nums) and then 
        # XOR it with all of the nums in the array and their indices
        # in the end we will be left with missing number
        # E.g.
        # Nums     0  1  3   4
        # indices  0  1  2   3
        # XOR will be as:
        # missing = 4 ^ (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 2) ^ (4 ^ 3)
        #         = (4^4) ^ ( 0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2  (if we rearrange for simplicity)
        #         = 0 ^ 0 ^ 0 ^ 0 ^ 2
        #         = 2  < --- This is our answer
        
        missing = len(nums)
        for i, v in enumerate(nums):
            missing ^= i ^ v
        return missing


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Gauss's formula for sum of `n` numbers is `n*(n+1)/2`
        n = len(nums)
        exp_sum = (n * (n+1))//2
        actual_sum = 0
        for n in nums:
            actual_sum += n
        
        return exp_sum - actual_sum
        