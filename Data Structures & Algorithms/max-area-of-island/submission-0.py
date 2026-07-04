class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0

        def dfs(grid, i, j):
            if not len(grid) - 1 >= i >= 0 or not len(grid[i]) - 1 >= j >= 0:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            return (
                1
                + dfs(grid, i + 1, j)
                + dfs(grid, i - 1, j)
                + dfs(grid, i, j + 1)
                + dfs(grid, i, j - 1)
            )

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    print(i,j)
                    max_area = max(max_area, dfs(grid, i, j))
        return max_area
