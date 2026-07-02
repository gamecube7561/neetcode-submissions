class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = {}
        rank = {}
        name = {}

        def get_par(node):
            while par[node] != node:
                node = par[node]
            return node
        
        for a in accounts:
            for i in range(1, len(a)):
                name[a[i]] = a[0]
                par[a[i]] = a[i]
                rank[a[i]] = 0

        for a in accounts:
            for i in range(2, len(a)):
                node1, node2 = get_par(a[i]), get_par(a[i-1])
                if node1 != node2:
                    if rank[node1] > rank[node2]:
                        par[node2] = node1
                    elif rank[node2] > rank[node1]:
                        par[node1] = node2
                    else:
                        par[node2] = node1
                        rank[node2] += 1 
        
        for node in par:
            par[node] = get_par(node)

        res_map = {}
        for node in par:
            if par[node] in res_map:
                res_map[par[node]].append(node)
            else:
                res_map[par[node]] = []
                res_map[par[node]].append(node)

        res = []
        for acc in res_map:
            temp = []
            temp.append(name[acc])

            for email in res_map[acc]:
                temp.append(email)
            res.append(temp)

        return res


        