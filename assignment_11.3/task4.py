"""
Simple hash table implementation with chaining for collision resolution.

Provides `insert`, `search`, and `delete` methods.  Keys are assumed to
be hashable and unique; values can be any object.  The table uses a
fixed number of buckets and stores entries in linked lists (Python
`list`s) when collisions occur.

Usage example in `__main__` demonstrates basic operations and collision
behavior.
"""

from __future__ import annotations
from typing import Any, List, Tuple


class HashTable:
    """Basic hash table with chaining collision handling."""

    def __init__(self, capacity: int = 8) -> None:
        """Initialize table with given number of buckets."""
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacity)]
        self._capacity = capacity

    def _bucket_index(self, key: Any) -> int:
        """Compute the index of the bucket for a given key."""
        return hash(key) % self._capacity

    def insert(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair in the table.

        If the key already exists, its value is replaced.  Otherwise the
        pair is appended to the appropriate bucket list.
        """
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key: Any) -> Any:
        """Return the value associated with `key`, or raise KeyError."""
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key: Any) -> None:
        """Remove the key-value pair with the given key.

        Raises KeyError if the key is not found.
        """
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)

    def __repr__(self) -> str:
        return f"HashTable(capacity={self._capacity}, buckets={self._buckets!r})"


# ------------------------------------------------------------------
# Demonstration of functionality
# ------------------------------------------------------------------

if __name__ == "__main__":
    table = HashTable(capacity=4)  # small to force collisions
    print("Initial table:", table)

    # insert several items, including ones that collide by bucket
    pairs = [("apple", 1), ("banana", 2), ("grape", 3), ("cherry", 4)]
    for k, v in pairs:
        print(f"insert {k} -> {v}")
        table.insert(k, v)

    print("Table after inserts:", table)

    # search existing and non-existing
    print("search apple:", table.search("apple"))
    try:
        print("search orange:", table.search("orange"))
    except KeyError:
        print("orange not found")

    # update a value
    table.insert("banana", 20)
    print("banana updated:", table.search("banana"))

    # delete a key
    table.delete("grape")
    print("after deleting grape:", table)

    # attempt to delete missing key
    try:
        table.delete("pear")
    except KeyError:
        print("pear not found, cannot delete")
