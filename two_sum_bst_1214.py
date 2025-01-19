'''
https://algo.monster/liteproblems/1214
'''
from typing import Optional
class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def in_order_traversal(root: Optional[TreeNode], index: int):
            if not root:
                return
            in_order_traversal(root.left, index)  
            values[index].append(root.val)  
            in_order_traversal(root.right, index) 


        values = [[], []]

        in_order_traversal(root1, 0)
        in_order_traversal(root2, 1)

        # Initialize pointers
        left_index, right_index = 0, len(values[1]) - 1
      
        # Use a two-pointer approach to find two elements that sum up to target
        while left_index < len(values[0]) and right_index >= 0:
            current_sum = values[0][left_index] + values[1][right_index]
            if current_sum == target:
                return True  
            if current_sum < target:
                left_index += 1  
            else:
                right_index -= 1  


        return False

# Example usage:
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
solution = Solution()
result = solution.twoSumBSTs(root1, root2, 6)
print(result)