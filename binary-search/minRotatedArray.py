class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        l, h = 0, len(nums) -1
        while l <= h:
            mid = l + (h-l) // 2
            # handle sorted array or array with all elements being same(although this leetcode problem doesn't allow all numbers to be same, all nums are expected to be unique)
            if nums[l] <= nums[h]: return nums[l]
            
            if ((mid ==0 or nums[mid] < nums[mid+1]) and
               (mid == len(nums)-1 or nums[mid] < nums[mid-1])):
                    return nums[mid]
            elif nums[mid-1] > nums[mid]:
            # elif nums[mid] < nums[mid+1]:
                h = mid - 1 
                # l = mid +1
            else:
                l = mid + 1
                # h = mid - 1 
        return -1