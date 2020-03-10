class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        rst = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= rst[-1][1]:
                # merge
                if intervals[i][1] > rst[-1][1]:
                    rst[-1][1] = intervals[i][1]
            else:
                # no intersect
                rst.append(intervals[i])
        
        return rst