from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()

                for addRow, addCol in directions:
                    newRow = row + addRow
                    newCol = col + addCol

                    if (newRow in range(ROWS) and newCol in range(COLS) and
                       (newRow, newCol) not in visited and
                       grid[newRow][newCol] == "1"):

                       queue.append((newRow,newCol))
                       visited.add((newRow,newCol))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited: 
                    bfs(r,c)
                    islands += 1
        return islands