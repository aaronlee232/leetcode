class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sortByLowerInterval(list):
            return list[0]
        intervals.sort(key=sortByLowerInterval)
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i-1][1] = max(intervals[i][1], intervals[i - 1][1])
                del intervals[i]
                i -= 1
            i += 1
        return intervals