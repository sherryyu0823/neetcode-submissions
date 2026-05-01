class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        cnt = 0
        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]== "0":
                        continue
                    if grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    cnt += 1
                    bfs(r, c)
        return cnt
