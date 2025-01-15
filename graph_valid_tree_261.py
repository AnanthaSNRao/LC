
'''
https://algo.monster/liteproblems/261
'''

from typing import List

class Solution:
    def validTree(self, num_nodes: int, edges: List[List[int]]) -> bool:
        # Helper function to find the root of a node 'x'.
        # Uses path compression to flatten the structure for faster future lookups.
        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])  # Path compression
            return parent[node]
      
        # Initialize the parent list where each node is initially its own parent.
        parent = list(range(num_nodes))
      
        # Iterate over all the edges in the graph.
        for node_1, node_2 in edges:
            # Find the root of the two nodes.
            root_1 = find_root(node_1)
            root_2 = find_root(node_2)
          
            # If the roots are the same, it means we encountered a cycle.
            if root_1 == root_2:
                return False
          
            # Union the sets - attach the root of one component to the other.
            parent[root_1] = root_2
          
            # Each time we connect two components, reduce the total number of components by one.
            num_nodes -= 1
      
        # A tree should have exactly one more node than it has edges.
        # After union operations, we should have exactly one component left.
        return num_nodes == 1