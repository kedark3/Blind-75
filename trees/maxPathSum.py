""" 
Approach: Use DFS recursion - postorder traversal (left,right,root)
With DFS, we traverse to left subtree, calculate max we can get from there
then to right subtree, calculate max we can get from there
DFS will return current Node value + max(left,rightsubtree)

BUT important thing to
note here is that we are allowed to split at only one node to take left and right both
and everywhere else we need to just select one node either left or right (or if they are negative
then choose none - 0)

Our result will be the maximum value we can get by splitting at a root node of
any of the subtrees or the main tree.

Our return value at each step to the parent will be what is the max we can get without
splitting. i.e. node.val + max(left,right,0)

Intuition: 
It helps to start at leaf nodes, 
because the max value will be the value of the leaf node iself as both left and right
will return 0.

TC: O(N) we only traverse the tree once
SC: O(logn) - height of the tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # by making res a reference, we can update it inside the 
        # dfs() function without having to use global or nonlocal
        res = [root.val]
        
        def dfs(node):
            #base 
            if not node:
                return 0
            
            # logic 
            left_max = dfs(node.left)  
            right_max = dfs(node.right) 
            # update result at each step, cause remember max sum can occur at any of the subtrees
            # it doesn't necessarily have to be at the root of the tree
            res[0] = max(res[0], node.val+left_max+right_max)
            
            # we return left and right max values, and 0 because if both of the left and right subtrees
            # are negative, then they will reduce our sum node.val + (some -ve value), hence we choose to make it 0
            # This is the value we get, without split, meaning if we were to just choose one subtree out of two
            return node.val + max(left_max, right_max, 0)
        
        dfs(root)
        return res[0]
    