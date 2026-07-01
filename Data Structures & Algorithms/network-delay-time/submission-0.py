class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, w in times:
            adj[s].append([d, w])
        
        shortest = {}
        min_heap = [[0, k]]

        while min_heap:
            weight1, node1 = heapq.heappop(min_heap)
            if node1 in shortest:
                continue

            shortest[node1] = weight1

            for node2, weight2 in adj[node1]:
                if node2 not in shortest:
                    heapq.heappush(min_heap, [weight1 + weight2, node2])
        
        if len(shortest) != n:
            return -1

        res = 0

        for key in shortest.keys():
            if shortest[key] == 0 and key != k:
                return -1
            res = max(res, shortest[key])

        return res
        