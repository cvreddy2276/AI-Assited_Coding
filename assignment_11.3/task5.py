"""
Campus Resource Management System design analysis and partial implementation.

Feature-to-data-structure mapping with justifications is included below.
One feature (Cafeteria Order Queue) is implemented in code as a working
Python module with demonstration.
"""



from __future__ import annotations
from collections import deque
from typing import Any, Deque


class CafeteriaQueue:
    """Simple FIFO queue for cafeteria orders."""

    def __init__(self) -> None:
        self._orders: Deque[Any] = deque()

    def enqueue(self, order: Any) -> None:
        """Place a new order at the end of the queue."""
        self._orders.append(order)

    def dequeue(self) -> Any:
        """Serve the next order (remove from front).

        Raises IndexError if the queue is empty.
        """
        return self._orders.popleft()

    def peek(self) -> Any:
        """Return the next order without serving it."""
        if not self._orders:
            raise IndexError("peek from empty queue")
        return self._orders[0]

    def is_empty(self) -> bool:
        return not self._orders

    def __len__(self) -> int:
        return len(self._orders)

    def __repr__(self) -> str:
        return f"CafeteriaQueue({list(self._orders)!r})"


# ------------------------------------------------------------------
# Demonstration
# ------------------------------------------------------------------

if __name__ == "__main__":
    queue = CafeteriaQueue()
    print("Starting cafeteria queue:", queue)

    # simulate customers placing orders
    for i in range(1, 6):
        order = {"customer": f"cust{i}", "items": ["sandwich", "juice"]}
        print("enqueue", order)
        queue.enqueue(order)

    print("Current queue:", queue)
    print("Next to serve (peek):", queue.peek())

    while not queue.is_empty():
        served = queue.dequeue()
        print("served", served)

    print("Queue after serving all orders:", queue)
