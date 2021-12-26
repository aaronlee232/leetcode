class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda a: math.sqrt(abs(a[0]) ** 2 + abs(a[1]) ** 2))
        return points[:k]