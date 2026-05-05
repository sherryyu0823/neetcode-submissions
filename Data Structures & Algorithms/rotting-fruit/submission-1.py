class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue  = deque()
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i, j))
                if grid[i][j]==1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        cnt = 0
        while queue and fresh>0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for r, c in dir:
                    ni = r + i
                    nj = c + j
                    if 0<=ni<row and 0<=nj<col and grid[ni][nj]==1:
                        queue.append((ni, nj))
                        grid[ni][nj] = 2
                        fresh -= 1

            cnt += 1
        
        if fresh == 0:
            return cnt
        else:
            return -1
