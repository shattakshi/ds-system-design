"""
Explanation:

I solved this problem in two parts:

1. can_attend_all(events):
- Sort events by start time
- Check for overlap between consecutive events

2. min_rooms_required(events):
- Use a min-heap to track end times
- If a meeting ends before next starts → reuse room
- Else → allocate new room

Heap size = number of rooms needed
"""

import heapq


def can_attend_all(events):
    events.sort()

    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False
    return True


def min_rooms_required(events):
    if not events:
        return 0

    events.sort()
    heap = []

    heapq.heappush(heap, events[0][1])

    for i in range(1, len(events)):
        if events[i][0] >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, events[i][1])

    return len(heap)