class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            s = set(nums1)
        else:
            s = set(nums2)
            
        l = nums1 if len(nums1) < len(nums2) else nums2
        res = set()
        for item in l:
            if item in s:
                res.add(item)
        return list(res)
                