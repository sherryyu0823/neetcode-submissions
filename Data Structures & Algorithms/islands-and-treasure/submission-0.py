class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure = deque()
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    treasure.append((r, c))

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while treasure:
            tr, tc = treasure.popleft()
            for dr, dc in dir:
                nr, nc = tr+dr, tc+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols:
                    continue
                
                if grid[nr][nc] == INF: 
                    treasure.append((nr, nc))
                    grid[nr][nc] = grid[tr][tc]+1
        
       