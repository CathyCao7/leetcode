def merge(self, intervals):
        # write your code here
        # sort the intervals by start
        intervals = sorted(intervals, key=lambda x: x.start)
        merged_intervals = []
        for interval in intervals:
            if len(merged_intervals) == 0 or merged_intervals[-1].end < interval.start:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1].end = max(interval.end, merged_intervals[-1].end)
        return merged_intervals
        else:
            return -1

            
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end: 
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result


if __name__ == "__main__":
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])
