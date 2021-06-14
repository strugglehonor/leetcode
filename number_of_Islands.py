class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):                
                if grid[i][j] == "1":
                    num += 1
                    self.dfs(grid, i, j)
        return num
    
    def dfs(self, grid, m, n):
        # 不在网格内或者为“0”则终止递归
        if not self.isInGrid(grid, m, n) or grid[m][n] == "0":
            return
        if grid[m][n] == "1":
            grid[m][n] = "0"
            # 遍历上下左右的网格
            self.dfs(grid, m-1, n)
            self.dfs(grid, m+1, n)
            self.dfs(grid, m, n-1)
            self.dfs(grid, m, n+1)

    def isInGrid(self, grid, i, j):
        return i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0 
