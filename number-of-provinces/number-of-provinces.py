class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionFind:
            def __init__ (self):
                self.f = {}
            
            # find parent
            def find(self, x) -> int:
                parent = self.f.get(x, x)
                # if parent is itself, root is reached
                # else can go further
                if parent == x:
                    # root is reached
                    self.f[x] = x
                    return x;
                else:
                    parent = self.find(parent)
                    self.f[x] = parent
                    return parent
            
            # merge two value's parents
            def union(self, x, y):
                parentX = self.find(x)
                parentY = self.find(y)
                self.f[parentX] = parentY
            
        uf = UnionFind()
        for i in range(len(isConnected)):
            for j in range(i, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
         
        groups = set()
        for i in range(len(isConnected)):
            groups.add(uf.find(i))
        
        return len(groups)
        
                
                
                
            
                