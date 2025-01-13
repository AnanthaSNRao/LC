'''
https://algo.monster/liteproblems/1102
'''
from typing import List

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        cells = [(value, row, col) for row, row_content in enumerate(grid) for col, value in enumerate(row_content)]
        cells.sort(reverse=True)

        answer = 0

        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        parent = list(range(m * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        while find(0) != find(m * n - 1):
            value, row, col = cells.pop()
            answer = value  
            visited.add((row, col))  
          
            for dr, dc in directions:
                rr = row + dr
                cc = col + dc
              
                if 0 <= rr < m and 0 <= cc < n and (rr, cc) in visited:
                    parent[find(rr * n + cc)] = find(row * n + col)
                  
        return answer
    

s = Solution()
mat = [[1,2,3,4,5,6], [7,8,9,1,2,3], [4,5,6,7,8,9], [1,2,3,4,5,6]]
print(s.maximumMinimumPath(mat))