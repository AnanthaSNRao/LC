'''
https://algo.monster/liteproblems/296
'''

from typing import List
class Solution:
    # Method to calculate the minimum total distance
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Helper function to calculate the distance to the median element 'median' from all elements in 'elements'
        def calculate_distance(elements, median):
            return sum(abs(element - median) for element in elements)

        # List to record the positions of '1's in rows and columns
        row_positions, col_positions = [], []

        # Loop through the grid to find positions of '1's
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                if cell:  # If the cell is '1', record its position
                    row_positions.append(row_index)
                    col_positions.append(col_index)

        # Sort the column positions to easily find the median
        col_positions.sort()

        # Find medians of rows and columns positions for '1'',s
        # since the list is sorted/constructed in order, the median is the middle value
        row_median = row_positions[len(row_positions) // 2]
        col_median = col_positions[len(col_positions) // 2]

        # Calculate the total distance using the median of rows and columns
        total_distance = calculate_distance(row_positions, row_median) + calculate_distance(col_positions, col_median)

        return total_distance
