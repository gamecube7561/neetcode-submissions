class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, i, j):
            edges = 0
            if 0 > i or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1
            edges += dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j-1)
            return edges
            
        edges = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    edges += dfs(grid, i, j)
        
        return edges