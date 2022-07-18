"""
Approach:
Intuition:
Cloning a graph means creating new nodes and adding neighbor nodes to
their neighbors list - and even all nodes in the neighbors list should 
be independently created new nodes.

Solution:
Use BFS/DFS to start traversing graph nodes and their neighbors. At each step
for each node - create a new copy using Node() constructor call and maintain
a mapping using hashmap where for each old node, we keep corresponding new node.
What this does is, we don't keep more copies of Node objects than that are needed.
Algorithm:
1) Start DFS on Node0. Create its copy, add it to hashmap, then iterate over its neighbors
2) For each neighbor, call DFS again, if the node already exists in the hashmap, return it
3) If it doesn't exist, create a copy, and iterate over its neigbors in the original node
4) populate neighbors list in new node and return the copy object
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_new = {}
        
        def dfs_clone(node):
            # base
            if not node:
                return None
            
            if node in old_new:
                return old_new[node]
            
            # logic
            copy = Node(node.val)
            old_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei))
                
            return copy

        return dfs_clone(node)