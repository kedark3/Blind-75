"""
Approach: Comput lp array, then use rp as int variable and compute output 
directly into lp array as lp[i] *= rp and update rp *= nums[i]

TC O(N)
SC O(1) as lp is output and it is not conted towards the SC.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1]*len(nums)
        
        for i in range(1,len(nums)):
            lp[i] = lp[i-1] * nums[i-1]
        
        rp =1
        for i in range(len(nums)-1, -1, -1):
            lp[i] *= rp
            rp *= nums[i]
        
        return lp

# approach 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        lp = 1
        for i in range(len(nums)):
            output[i] = lp
            lp *= nums[i]
        
        rp = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= rp
            rp *= nums[i]
        
        # print(lp,rp)
        # print(nums)
        return output

# approach 3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp, rp = [1]*len(nums), [1]*len(nums)
        
        for i in range(1,len(nums)):
            lp[i] = lp[i-1] * nums[i-1]
            
        for i in range(len(nums)-2,-1,-1):
            # print(i)
            rp[i] = rp[i+1] * nums[i+1]
        
        # print(lp,rp)
        
        for i in range(len(nums)):
            nums[i] = lp[i] * rp[i]
        
        # print(nums)
        return nums