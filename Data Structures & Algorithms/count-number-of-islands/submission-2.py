class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(r, c):
            if r>=row or r <0 or c>=col or c <0:
                return
            if grid[r][c] == '0':
                return
            if grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r-1, c)
                dfs(r, c-1)
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt

