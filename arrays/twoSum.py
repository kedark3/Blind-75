class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force O(n^2)
        # r = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             r.append(i)
        #             r.append(j)
        
        
        # Two pass hashmap
#         m = {nums[i]: i for i in range(len(nums))}
#         for i,num in enumerate(nums):
#             try:
#                 # check if the target-num(complement)
#                 # exist in the hashmap, if yes, check its
#                 # value is not same as current index
#                 # e.g. it will fail otherwise for:[1,3,4,2] target 6
#                 if m[target-num] != i :
#                     # if all of that is good, return i and m[complement]q
#                     return [i, m[target-num]]
#             except KeyError:
#                 continue
                
        
        # One pass hashmap
        m = dict()
        for i, num in enumerate(nums):
            if target - num not in m:
                m[num] = i
            else:
                return [m[target-num], i]
            
        # two pointers
        # this will only work on sorted Arrays
        # low = 0
        # high = len(nums) - 1
        # nums = sorted(nums)
        # while low < high:
        #     if nums[low] + nums[high] == target:
        #         return [low, high]
        #     if nums[low] + nums[high] < target:
        #         low += 1
        #     if nums[low] + nums[high] > target:
        #         high -= 1

        
     
        return -1