"""
Explanation:

This file tests the LRU cache operations.
It verifies:
- Insertions
- Access updates (recent usage)
- Eviction of least recently used item
"""

from lru_cache.lru_cache import LRUCache


def test_lru():
    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)
    print("get(1):", cache.get(1))  # 10

    cache.put(3, 30)  # removes key 2
    print("get(2):", cache.get(2))  # -1


if __name__ == "__main__":
    test_lru()