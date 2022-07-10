class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}  # create adj list for each of the n nodes
        
        for e1,e2 in edges:  # add edges to adj list
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        # define dfs
        visited = set()
        def dfs(curr, prev):
            # we already visited this node means there maybe a loop
            if curr in visited:
                return False
            # if node was not visited, add it to visited
            visited.add(curr)
            # check all of its neighbors and run dfs on it to determine if they are visited or not.
            for neighbor in adj[curr]:
                if neighbor == prev:  # so we don't keep visiting the node that we came from
                    continue
                if not dfs(neighbor, curr):  # if dfs on neighbor returned False- meaning it has been alrady visited by somewhere else,
                    # end dfs and return immediately
                    return False
            return True
        #  n == len(visited) should be True unless there is a node that is disconnected from rest of the tree/graph
        # that will cause node to not ever be visited and our visited set will be shorter than `n`
        return dfs(0,-1) and n == len(visited)
            