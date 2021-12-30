class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertexCount = {}
        for edge in edges:
            vertexCount[edge[0]] = vertexCount.get(edge[0], 0) + 1
            vertexCount[edge[1]] = vertexCount.get(edge[1], 0) + 1

        maxV = list(vertexCount.keys())[0]
        for v in vertexCount:
            if (vertexCount[v] > vertexCount[maxV]):
                maxV = v
        return maxV