class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        visited = {}
        

        for i in range(n):
            adj[i] = []
            visited[i] = -1
        
        for e in edges:
            adj[e[0]].append((e[1], e[2]))

        
        visited[src] = 0
        stack = []

        for e in adj[src]:
            heapq.heappush(stack, (e[1], e[0]))

        
        while stack:
            weight, node = heapq.heappop(stack)
    
            if node in visited and visited[node] != -1:
                continue

            visited[node] = weight

            for e in adj[node]:
                heapq.heappush(stack, (e[1] + weight, e[0]))

        return visited
            
