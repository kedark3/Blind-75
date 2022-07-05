from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # BFS
        q = deque()
        q.append(root)
        lvl = 0
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        return lvl
            
        
        # DFS Recursive
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # DFS Iterative
#         stack= []
#         stack.append((root, 1))
#         maxDepth = 0
        
#         while stack:
#             node, d = stack.pop()
#             maxDepth = max(maxDepth, d)
#             if node.left:
#                 stack.append((node.left, d+1))
#             if node.right:
#                 stack.append((node.right, d+1))
#         return maxDepth


            