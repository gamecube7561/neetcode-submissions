"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda k: k.start)
        end_time = 0
        for interval in intervals:
            if interval.start < end_time:
                return False
            end_time = max(end_time, interval.end)

        return True
