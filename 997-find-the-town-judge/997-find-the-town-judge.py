class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # non-zero based indexing
        trustScore = [0] * (n + 1)
        
        for person in trust:
            trustScore[person[0]] -= 1
            trustScore[person[1]] += 1
        
        for person in range(1, n + 1):
            if trustScore[person] == n - 1:
                return person
        return -1
        