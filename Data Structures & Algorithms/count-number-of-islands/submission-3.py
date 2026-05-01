class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def BFS(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = '0' #visited
            while queue:
                rr, cc = queue.popleft()
                for dr, dc in dir:
                    nr = rr+dr
                    nc = cc+dc
                    if nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]=='1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    BFS(i, j)
        return cnt
