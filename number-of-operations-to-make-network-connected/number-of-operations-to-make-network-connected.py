class UnionFind:
    def __init__(self):
        self.f = {}
        
    def find(self, x):
        parent = self.f.get(x, x)
        if parent == x:
            return x
        else:
            self.f[x] = self.find(parent)
            return self.f[x]
        
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        
        self.f[parentX] = parentY
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind()
        for connection in connections:
            uf.union(connection[0], connection[1])
        
        groups = set()
        for i in range(n):
            groups.add(uf.find(i))

            
        if n - 1 <= len(connections):
            return len(groups) - 1
        else:
            return -1
        
        
        