class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = {}
        par = {}

        def get_par(node):
            while par[node] != node:
                node = par[node]
            return node

        for i in range(0, n):
            par[i] = i
            rank[i] = 0
        
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
    

        par_set = set()
        for n in par:
            par_set.add(get_par(par[n]))

        return len(par_set)


        