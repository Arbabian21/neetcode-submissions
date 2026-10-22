class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, ocean, prevHeight):
            if (row < 0 or col < 0 or
                row == ROWS or col == COLS or
                heights[row][col] < prevHeight or
                (row, col) in ocean): return

            ocean.add((row, col))
            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])
            

    
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res