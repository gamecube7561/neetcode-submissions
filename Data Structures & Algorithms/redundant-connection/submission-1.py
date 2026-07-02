class Solution:


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        def get_par(node):
            while par[node] != node:
                node = par[node]
            return node

        nodes = 0

        for e in edges:
            nodes = max(nodes, e[0])
            nodes = max(nodes, e[1])
        
        for i in range(1, nodes + 1):
            par[i] = i
            rank[i] = 0

        ret = []

        for e in edges:
            par1, par2 = get_par(e[0]), get_par(e[1])
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    par[par2] = par1
                elif rank[par2] > rank[par1]:
                    par[par1] = par2
                else:
                    par[par1] = par2
                    rank[par2] += 1
            else:
                ret = e

        return ret