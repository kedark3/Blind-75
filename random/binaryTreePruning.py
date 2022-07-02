# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # use DFS
        def containsOne(node):
            # base
            if not node:
                return False
            
            # logic
            left = containsOne(node.left)
            right = containsOne(node.right)
            # if left or right are False, then set node.left/right to None
            if not left:
                node.left = None
            if not right:
                node.right = None
            # return value of current node or left or right
            # if any of them is 1 or True we return True, else False
            return node.val or left or right
        
        containsOne(root)
        return root