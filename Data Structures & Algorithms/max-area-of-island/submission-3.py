class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        ans = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            cnt = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    
                    if nc<0 or nr<0 or nr>=rows or nc>=cols or grid[nr][nc] == 0:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        cnt += 1
            return cnt
            
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1:
                    cnt = bfs(r, c) 
                    ans = max(ans, cnt)
        
        return ans
        