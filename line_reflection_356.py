from typing import List, Optional
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # Initialize minimum and maximum X to positive and negative infinity respectively.
        min_x, max_x = float('inf'), float('-inf')
        point_set = set()  # Create a set to store unique points.

        # Iterate over all points to find the min and max X values and add points to the set.
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))

        # Calculate the sum of min and max X, which should be equal to twice the X value of the reflection line.
        reflection_sum = min_x + max_x

        # Check if for each point (x, y), the reflected point across the Y-axis
        # given by (reflection_sum - x, y) exists in the point set.
        # The reflection across the Y-axis is defined by the line X = (min_x + max_x) / 2.
        return all((reflection_sum - x, y) in point_set for x, y in points)