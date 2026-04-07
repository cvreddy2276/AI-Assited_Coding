"""
Library request management for SRU.

This module provides two queue implementations:

- Simple FIFO `Queue` for managing book borrow requests.
- `PriorityQueue` which gives priority to faculty requests over students.

Each queue supports `enqueue` and `dequeue` operations. A basic demo
is included under `__main__`.
"""

from __future__ import annotations
from collections import deque
from typing import Any, Deque, List, Tuple


class Queue:
    """Simple FIFO queue using collections.deque."""

    def __init__(self) -> None:
        self._items: Deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Remove and return the item at the front of the queue.

        Raises IndexError if the queue is empty.
        """
        return self._items.popleft()

    def is_empty(self) -> bool:
        return not self._items

    def __repr__(self) -> str:
        return f"Queue({list(self._items)!r})"


class PriorityQueue:
    """Priority queue with two levels: faculty > student.

    Internally maintains two FIFO queues; items are tuples
    `(category, request)` where category is one of the strings
    `'faculty'` or `'student'`.  Dequeue always returns the oldest
    faculty request if any exist, otherwise falls back to student.
    """

    def __init__(self) -> None:
        self._faculty: Deque[Any] = deque()
        self._student: Deque[Any] = deque()

    def enqueue(self, category: str, request: Any) -> None:
        """Add a request under the given category.

        Category must be either 'faculty' or 'student'.
        """
        cat = category.lower()
        if cat == "faculty":
            self._faculty.append(request)
        elif cat == "student":
            self._student.append(request)
        else:
            raise ValueError("Category must be 'faculty' or 'student'")

    def dequeue(self) -> Tuple[str, Any]:
        """Remove and return the highest priority request.

        Returns a tuple `(category, request)`.  Raises IndexError if no
        requests remain.
        """
        if self._faculty:
            return ("faculty", self._faculty.popleft())
        if self._student:
            return ("student", self._student.popleft())
        raise IndexError("dequeue from empty priority queue")

    def is_empty(self) -> bool:
        return not (self._faculty or self._student)

    def __repr__(self) -> str:
        return (
            f"PriorityQueue(faculty={list(self._faculty)!r}, "
            f"student={list(self._student)!r})"
        )


# ------------------------------------------------------------------
# Simple demonstration / test code
# ------------------------------------------------------------------

if __name__ == "__main__":
    # FIFO queue example
    print("=== FIFO queue demo ===")
    q = Queue()
    for name in ["req1", "req2", "req3"]:
        print("enqueue", name)
        q.enqueue(name)
    while not q.is_empty():
        print("dequeue", q.dequeue())

    # Priority queue example
    print("\n=== Priority queue demo ===")
    pq = PriorityQueue()
    # mixed requests: tuple(description)
    pq.enqueue("student", "stud-1")
    pq.enqueue("faculty", "fac-1")
    pq.enqueue("student", "stud-2")
    pq.enqueue("faculty", "fac-2")

    while not pq.is_empty():
        cat, req = pq.dequeue()
        print(f"dequeue {cat}: {req}")
