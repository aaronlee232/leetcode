class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # non-zero based indexing
        trustsNobody = [True] * (n + 1)
        trustCount = [0] * (n + 1)
        
        for person in trust:
            trustsNobody[person[0]] = False
            trustCount[person[1]] += 1
        
        for person in range(1, n + 1):
            if trustsNobody[person] and trustCount[person] == n - 1:
                return person
        return -1
        