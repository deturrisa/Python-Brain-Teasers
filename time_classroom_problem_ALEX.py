class ClassRoom(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def overlapping(classRoomA, classRoomB):
    if classRoomA.start > classRoomB.end:
        return False
    elif classRoomA.end < classRoomB.start:
        return False
    return True


intervals = [ClassRoom(30, 75), ClassRoom(0, 50), ClassRoom(60, 150)]
rooms_needed = 0

for i in range(len(intervals) - 1):
    for j in range(i + 1, len(intervals)):
        if overlapping(intervals[i], intervals[j]):
            rooms_needed += 1

print(rooms_needed)
