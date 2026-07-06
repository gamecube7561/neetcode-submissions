class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = {}
        for i in range(len(grid)):
            adj[i] = {}
            for j in range(len(grid[i])):
                adj[i][j] = []
                adj[i][j].append((i + 1, j))
                adj[i][j].append((i - 1, j))
                adj[i][j].append((i, j + 1))
                adj[i][j].append((i, j - 1))

        visited = set()
        stack = []
        heapq.heappush(stack, (0, 0, 0))

        water_level = grid[0][0]

        while stack:
            weight, i, j = heapq.heappop(stack)

            if ((i, j)) in visited:
                continue
            water_level = max(water_level, weight)
            if ((i, j)) == ((len(grid)-1, len(grid[0])-1)):
                break
            
            for e in adj[i][j]:
                if (
                    e[0] < 0
                    or e[0] > (len(grid) - 1)
                    or e[1] < 0
                    or e[1] > (len(grid[0]) - 1)
                    or ((e[0], e[1])) in visited
                ):
                    continue
                
                heapq.heappush(stack, (grid[e[0]][e[1]], e[0], e[1]))
            
            visited.add((i, j))

        return water_level
