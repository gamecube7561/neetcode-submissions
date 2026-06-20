class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        return True
        

    def getNumComponents(self) -> int:
        num_comp = 0
        for p in self.parent:
            if p == self.parent[p]:
                num_comp += 1
        return num_comp
