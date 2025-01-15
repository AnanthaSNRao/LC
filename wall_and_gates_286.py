
'''
https://algo.monster/liteproblems/286
'''

from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        """
        This method modifies the 'rooms' matrix in-place by filling each empty room with the distance to its nearest gate.
      
        An empty room is represented by the integer 2**31 - 1, a gate is represented by 0, and a wall is represented by -1.
      
        :type rooms: List[List[int]]
        """
        num_rows, num_cols = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        queue = deque([(row, col, 0) for row in range(num_rows) for col in range(num_cols) if rooms[row][col] == 0])
    
    
        while queue:
            i, j, distance = queue.popleft()

            for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = i + delta_row, j + delta_col
                
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and rooms[new_row][new_col] != -1:
                    rooms[new_row][new_col] = min(distance+1, rooms[new_row][new_col])
                    queue.append((new_row, new_col, distance+1))
        return rooms


