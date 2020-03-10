class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        merged = []
        i = 0
        while i < len(intervals) and intervals[i][0] <= newInterval[0]:
            merged.append(intervals[i])
            i += 1

        intervals.insert(i, newInterval)
        while i < len(intervals):
            if len(merged) == 0:
                merged.append(intervals[i])
                continue
                
            if intervals[i][0] <= merged[-1][1]:
                # merge
                if intervals[i][1] > merged[-1][1]:
                    merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i]) 
            i += 1

        return merged