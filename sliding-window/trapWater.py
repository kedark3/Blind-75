# Approach : Trap Water - Linear algo and O(n) space
# - Traverse on array left to right and at each index note the max so far
# - Traverse on array right to left and at each index note the max so far
# - Traverse 3rd time and at each location, check what is the min of left and right max and subtract current height from it
#   - If it is greater than 0 add to answer else add 0 to answer
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []  # O(n) space
        right_max = [0]*len(height)  # O(n) space
        max_so_far = 0
        for i, h in enumerate(height):
            max_so_far = max(max_so_far,h)
            left_max.append(max_so_far)
        
        max_so_far = 0
        for i in range(len(height)-1, -1, -1):
            max_so_far = max(max_so_far,height[i])
            right_max[i] = max_so_far
        
        # print(left_max)
        # print(right_max)
        result = 0
        
        for i, h in enumerate(height):
            result += max(min(left_max[i],right_max[i])-h, 0)
        return result


# Approach 2: O(1) space and linear time
# In this appraoch we need to move left and right pointers such that, depending on if the 
# left_max is smaller or right max is smaller, because maximum water is at any index is bounded by
# whatever is the smaller max value. 
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        
        l, h = 0, len(height) - 1
        
        l_max, r_max = height[l], height[h]
        ans = 0
        
        while l < h:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
            else:
                h -= 1
                r_max = max(r_max, height[h])
                ans += r_max - height[h]
        return ans