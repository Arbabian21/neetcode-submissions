class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word): return True # you found the word
            if (r < 0 or c < 0 or # you are no longer in the board
                r >= ROWS or c >= COLS or # you are no longer in thee board
                word[i] != board[r][c] or # you are at the wrong letteer so why eeven worry about it
                (r,c) in path): # you've already beeeen heere beforee
                return False

            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or # samee collumn but further down the row
                   dfs(r - 1, c, i + 1) or # same collumn but go back in this row
                   dfs(r, c + 1, i + 1) or # same row but move along the ocllumn
                   dfs(r, c - 1, i + 1)) # same row but move to up thee collumn
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False