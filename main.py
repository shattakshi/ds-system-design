"""
Explanation:

This file runs both modules together for demonstration.
"""

from lru_cache.lru_cache import LRUCache
from scheduler.scheduler import can_attend_all, min_rooms_required


# LRU Demo
cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print("LRU get(1):", cache.get(1))

cache.put(3, 30)
print("LRU get(2):", cache.get(2))


# Scheduler Demo
events = [(9, 10), (10, 11), (11, 12)]
print("Can attend all:", can_attend_all(events))

events2 = [(9, 11), (10, 12)]
print("Can attend all:", can_attend_all(events2))
print("Rooms needed:", min_rooms_required(events2))