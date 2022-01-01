class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        
        def getNeighbors(grid, x, y):
            neighbors = []
            dx = [0, 1, 0, -1, 1, 1, -1, -1]
            dy = [1, 0, -1, 0, 1, -1, 1, -1]
            
            for i in range(len(dx)):
                newX = dx[i] + x
                newY = dy[i] + y
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 0:
                    neighbors.append((newX, newY))
            return neighbors
        
        # bfs
        end = (len(grid) - 1, len(grid[0]) - 1)
        
        visited = set()
        level = 1
        
        queue = [(0,0)]
        visited.add((0,0))
        while queue:
            nextLevel = []
            for coord in queue:
                if coord == end: return level
                for coord in getNeighbors(grid, coord[0], coord[1]):
                    if coord not in visited:
                        visited.add(coord)
                        nextLevel.append(coord)
            level += 1
            queue = nextLevel
        return -1    