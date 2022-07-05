# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:              
    def __init__(self):
        self.i = self.res = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return True

        def traverse(node):
            if not node: 
                return 
            traverse(node.left)
            if node:
                self.i += 1
            if self.i == k:
                self.res = node.val
                return
            traverse(node.right)
        traverse(root)
        return self.res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:              
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0
        while curr or stack:  # while curr is not None or stack is not empty
            while curr:  # while curr is valid, push curr on to the stack and move to left
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() # after all left childs are done, pop out the stack top
            n += 1 # increase n by 1
            if n == k:  # if its eq to k, return
                return curr.val
            curr = curr.right # move curr to right of curr node
     
