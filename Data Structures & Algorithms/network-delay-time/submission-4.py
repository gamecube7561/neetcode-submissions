class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for e in times:
            adj[e[0]].append([e[1], e[2]])

        minheap = []
        visited = {}
        heapq.heappush(minheap, [0, k])
        while minheap:
            
            weight, node = heapq.heappop(minheap)
            
            if node in visited:
                continue
            
            for e in adj[node]:
                heapq.heappush(minheap, [weight + e[1], e[0]])

            visited[node] = weight

        if len(visited) != n:
            return -1 
        else:
            res = 0
            for n in visited:
                res = max(res, visited[n])
            return res
        
