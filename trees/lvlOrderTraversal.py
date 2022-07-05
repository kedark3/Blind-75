"""
Approach: Queue approach

TC O(N) each node processed once
SC O(N) for queue = at any point queue will have at most N/2 nodes for a complete BST
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []
        
        q = deque()
        # append root
        q.append(root)
        while len(q) != 0:
            r = []
            for _ in range(len(q)):  # use for loop because we want to only iterate over 1 level at a time. If we use while loop, it will not end until all levels are finished and we will get only 1 list in result for all levelv combined.
                node = q.popleft()
                r.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(r)
        print(result)
        return result
                            