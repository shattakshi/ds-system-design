# Data Structures & Systems Design Assignment

## 📌 Overview
This project implements two core problems:
1. LRU Cache with O(1) operations
2. Event Scheduler for overlap detection and room allocation

The code is structured in a modular way with separate folders for each problem and dedicated test files.

---

## 📂 Project Structure


ds_system_design/
│
├── lru_cache/
│ ├── lru_cache.py
│ └── test_lru.py
│
├── scheduler/
│ ├── scheduler.py
│ └── test_scheduler.py
│
├── README.md
└── main.py


---

## 🚀 Problem 1: LRU Cache

### 🔹 Approach
The LRU Cache is implemented using:
- **Hash Map (Dictionary)** → for O(1) lookup
- **Doubly Linked List** → to maintain order of usage

### 🔹 Key Idea
- Most recently used items are moved to the front
- Least recently used items remain at the end
- When capacity is exceeded → remove from the end

### 🔹 Operations
- `get(key)` → returns value and marks as recently used
- `put(key, value)` → inserts/updates and handles eviction

### 🔹 Complexity
- Time: **O(1)** for both get and put
- Space: **O(n)**

---

## 📅 Problem 2: Event Scheduler

### 🔹 Functions

#### 1. can_attend_all(events)
- Sort events by start time
- Check if any event overlaps with the previous one

#### 2. min_rooms_required(events)
- Use a **min-heap** to track end times
- Reuse room if meeting ends before next starts
- Otherwise allocate new room

### 🔹 Key Idea
The heap always stores active meetings. Its size represents the number of rooms needed.

### 🔹 Complexity
- Time: **O(n log n)** (due to sorting + heap)
- Space: **O(n)**

---

## ⚖️ Trade-offs

A combination of:
- **Hash Map** → fast lookup
- **Doubly Linked List** → order maintenance

is used in LRU Cache to ensure constant time operations.

Using only one of these would either lose ordering or efficiency.

---

## 🔮 Future Improvements

### Room Assignment
Instead of only counting rooms:
- Store `(end_time, room_id)` in heap
- Assign actual room labels (Room A, Room B, etc.)

---

## 🔒 Concurrency (Thread Safety)

To make LRU Cache thread-safe:
- Use locks (mutex) to protect shared data
- Ensure only one thread modifies the cache at a time

---

## ▶️ How to Run

Run main file:

python main.py


Run tests:

python -m lru_cache.test_lru
python -m scheduler.test_scheduler


---

## ✅ Conclusion

This project demonstrates:
- Efficient use of data structures
- Clean modular design
- Scalable and testable implementation
- Strong understanding of algorithmic problem-solving