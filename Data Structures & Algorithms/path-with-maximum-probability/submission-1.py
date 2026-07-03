class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}

        for i in range(0, n):
            adj[i] = []

        for i in range(0, len(edges)):
            node1, node2, weight = edges[i][0], edges[i][1], succProb[i]
            adj[node1].append([weight, node2])
            adj[node2].append([weight, node1])

        visited = {}
        heap = []
        heapq.heappush(heap, [-1, start_node])

        while heap:
            weight, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited[node] = weight

            for e in adj[node]:
                heapq.heappush(heap, [weight * (e[0]), e[1]])
            
        if end_node in visited:
            return -visited[end_node]

        return 0