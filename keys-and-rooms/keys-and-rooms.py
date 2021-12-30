class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([rooms[0]])
        visited = set()
        visited.add(0)
        while queue:
            cur = queue.popleft()
            for room in cur:
                if room not in visited:
                    queue.append(rooms[room])
                    visited.add(room)
        
        return len(visited) == len(rooms)