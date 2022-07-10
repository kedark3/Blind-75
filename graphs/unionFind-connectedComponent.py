class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n):
            p = par[n] # parent of n is p
            while p != par[p]: # but if parent of p is not same as p
            # then update p to par[p] . E.g. par[2] = 1, but par[1] = 0, then p = par[1] = 0
            # this means par[2] is ultimately 0
                p = par[p]
            return p
           
    
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            # if both nodes have same parents, we don't need to do anything
            if p1 == p2:
                return 0
            # if both have different parents, then check which parent has higher rank
            # and add rank of lower parent to higher parent,
            # then set par[lower_rank_parent] = higher_rank_parent
            # e.g. if rank of 0(2) is greater than rank of 1(1), then make rank0=2+1 = 3, then par[p2] = p1, i.e. par[1] = 0
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return 1  # since we. merged edges, return 1
            
        for n1,n2 in edges:
            n -= union(n1,n2) # for every edge, see if we merged edges, if we did, then reduce count by 1, else don't

        return n # return count