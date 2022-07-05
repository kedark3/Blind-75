# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        left = self.isValidBST(root.left)
        # previous value should always be smaller than current, if not, we have inValid BST
        if self.prev and root.val <= self.prev.val:
            return False
        # if prev is not set, set it to current node before going down to the right subtree
        self.prev = root

        right = self.isValidBST(root.right)
        
        return left and right
    
    
        
        