"""
IT Help Desk ticket manager using a stack (LIFO).

Tickets arrive sequentially but are escalated in LIFO order.  This
module implements a simple stack with the required operations and
simulates handling five tickets.  Additional utility methods include
checks for emptiness and a (configurable) maximum size.
"""

from __future__ import annotations
from typing import Any, List, Optional


class TicketStack:
    """Stack for managing support tickets."""

    def __init__(self, max_size: Optional[int] = None) -> None:
        self._stack: List[Any] = []
        self._max_size = max_size

    def push(self, ticket: Any) -> None:
        """Add a ticket to the top of the stack.

        Raises OverflowError if the stack is full (when max_size is set).
        """
        if self._max_size is not None and len(self._stack) >= self._max_size:
            raise OverflowError("Stack is full")
        self._stack.append(ticket)

    def pop(self) -> Any:
        """Remove and return the ticket at the top of the stack.

        Raises IndexError if the stack is empty.
        """
        return self._stack.pop()

    def peek(self) -> Any:
        """Return the ticket at the top without removing it."""
        if not self._stack:
            raise IndexError("peek from empty stack")
        return self._stack[-1]

    def is_empty(self) -> bool:
        return not self._stack

    def is_full(self) -> bool:
        if self._max_size is None:
            return False
        return len(self._stack) >= self._max_size

    def __len__(self) -> int:
        return len(self._stack)

    def __repr__(self) -> str:
        return f"TicketStack({self._stack!r}, max_size={self._max_size!r})"


# ------------------------------------------------------------------
# Demonstration of stack behavior
# ------------------------------------------------------------------

if __name__ == "__main__":
    stack = TicketStack()
    print("Initial stack (should be empty):", stack)

    # simulate five tickets being raised
    for i in range(1, 6):
        ticket = f"ticket-{i}"
        print("push", ticket)
        stack.push(ticket)

    print("Current top (peek):", stack.peek())
    print("Stack after pushes:", stack)
    print("Is empty?", stack.is_empty())
    print("Is full?", stack.is_full())

    # resolve tickets in LIFO order
    while not stack.is_empty():
        resolved = stack.pop()
        print("pop (resolved):", resolved)

    print("Final stack (should be empty):", stack)
