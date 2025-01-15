
'''
https://algo.monster/liteproblems/314
'''

from collections import deque, defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list.
        if not root:
            return []

        # Initialize a double-ended queue to hold nodes along with their horizontal distances.
        node_queue = deque([(root, 0)])
        # Use a default dictionary to map horizontal distances to list of node values.
        column_table = defaultdict(list)

        # Perform a breadth-first search.
        while node_queue:
            # Process nodes level by level.
            for _ in range(len(node_queue)):
                current_node, horizontal_distance = node_queue.popleft()
                # Append the node's value to the list of its respective horizontal distance.
                column_table[horizontal_distance].append(current_node.val)

                # If the left child exists, add it to the queue with the horizontal distance decremented.
                if current_node.left:
                    node_queue.append((current_node.left, horizontal_distance - 1))
                # If the right child exists, add it to the queue with the horizontal distance incremented.
                if current_node.right:
                    node_queue.append((current_node.right, horizontal_distance + 1))

        # Sort the dictionary by horizontal distance and return the vertical order traversal.
        return [values for _, values in sorted(column_table.items())]
