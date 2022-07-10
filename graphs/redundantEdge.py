class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)
        def find(node):
            # finds parent of a node
            p = par[node]
            
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            # if both parents are same, edge don't need to be merged, it is redundant
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True

        
        for n1,n2 in edges:
            if not union(n1,n2): # if union returned False, means that is our redundant edge, return it
                return [n1,n2]