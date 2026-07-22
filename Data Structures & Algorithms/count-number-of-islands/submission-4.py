class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cnt = 0
        def DFS(i, j):

            if grid[i][j] == "1":
                grid[i][j] = "0"

                if i < len(grid)-1:
                    DFS(i+1, j)
                if i > 0:
                    DFS(i-1, j)

                if j < len(grid[0])-1:
                    DFS(i, j+1)
                if j > 0:
                    DFS(i, j-1)
            
            else:
                return



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    DFS(i, j)
                    cnt+=1
        
        return cnt