"""
Approach: Graph and Topological Sort
This is a graph problem. We need to mark following observations from the problem statement:
- if two words s & t have same prefix and t is shorter than s, then its invalid order, return "" - no solution
- In order to produce the answer, we need to compare each pair of words and use first "differing" character between w1 and w2 to create an adjescency list(or rather set) based hashmap
- Once hashmap is created, we run DFS on each of the node in the graph and create topological sort to produce the output

TC: O(C) - There were three parts to the algorithm; identifying all the relations, putting them into an adjacency list, and then converting it into a valid alphabet ordering.
In the worst case, the first and second parts require checking every letter of every word (if the difference between two words was always in the last letter). This is O(C). Third part is O(V+E) -> DFS on graph

SC: O(1) unless you count aux space of Adj list, which is O(V+E)
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Let's pre-populate adj list with chars from each of the words
        adj = {c:set() for word in words for c in word}
        # print(adj)
        
        # iterate over each pair of words and find first differing character
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1),len(w2))
            # if both words have same prefix and second word is shorter
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            # iterate over shorter word
            for j in range(minLen):
                if w1[j] != w2[j]:  # if we find non-matching chars
                    # then only we need to add it to adj set
                    adj[w1[j]].add(w2[j])
                    # also break the loop as we no need to go any further
                    break
        
        # Topological sort
        path, visited = set(), set()
        result = []
        def dfs(ltr):
            # if curr crs is already in path, that means there's a loop
            # return False in that case as we can't take that crs
            if ltr in path:
                return False
            if ltr in visited:
                return True
            
            # add each crs to path set
            path.add(ltr)
            # visit its prereqs
            for nei in adj[ltr]:
                # if any prereq was already in path, it will return False
                # that indicates cycle in the graph
                if dfs(nei) == False:
                    return False
            # if we didn't return due to cycle, means crs can be taken, make its
            # prereq list empty - meaning it is all taken and remove it from path set
            path.remove(ltr)
            visited.add(ltr)
            result.append(ltr)
            return True
        
        for ltr in adj.keys():
            if not dfs(ltr): # we detected a cycle
                return "" # which means there's no valid order that can be found
        # if we made it here, we reverse the result because rememeber, topological
        # sort (post order DFS) gives us the reverse order, we need to make it
        # correct before we join it as a string and return
        return ''.join(reversed(result))