class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        def dfs(grid, i, j):
            if not len(grid)-1 >= i >= 0 or not len(grid[0])-1 >= j >= 0 :
                return
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(grid, i, j)

        return island_count