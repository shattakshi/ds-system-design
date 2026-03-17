"""
Explanation:

This file tests both scheduler functions:
- Checks overlapping logic
- Verifies correct number of rooms
"""

from scheduler.scheduler import can_attend_all, min_rooms_required


def test_scheduler():
    events1 = [(9, 10), (10, 11), (11, 12)]
    print("Can attend all:", can_attend_all(events1))  # True

    events2 = [(9, 11), (10, 12)]
    print("Can attend all:", can_attend_all(events2))  # False
    print("Rooms required:", min_rooms_required(events2))  # 2


if __name__ == "__main__":
    test_scheduler()