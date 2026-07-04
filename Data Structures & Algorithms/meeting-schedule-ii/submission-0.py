"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda k: k.start)
        if not intervals:
            return 0

        rooms = 0
        room_set = set()

        for interval in intervals:
            temp = 1
            start_time = interval.start
            for room in room_set:
                if room[1] > start_time:
                    temp += 1
                    start_time = max(start_time, room[0])
            rooms = max(rooms, temp)
            room_set.add((interval.start, interval.end))

        return rooms