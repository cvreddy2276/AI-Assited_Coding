"""
Contact Manager Application for SR University student club.

The module provides two implementations of a simple contact manager:

1. Array (list) based using Python's built-in list.
2. Singly linked list based for dynamic allocation.

Supported operations:
 - add_contact(name, phone)
 - search_contact(name) -> phone or None
 - delete_contact(name) -> bool

At the end, basic comparison of efficiency for insertion and deletion
between the two approaches is provided.

Usage is demonstrated in the `__main__` section with simple examples.
"""

from __future__ import annotations
from typing import Optional


class Contact:
    """Simple data structure for storing contact information."""

    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def __repr__(self) -> str:
        return f"Contact(name={self.name!r}, phone={self.phone!r})"


# ----------------------------------------
# Array/List based implementation
# ----------------------------------------

class ArrayContactManager:
    """Contact manager backed by a Python list.

    Internally stores `Contact` objects in a list.  Addition is simply
    an append operation, search is a linear scan, and deletion is a
    linear search followed by removal.  The list automatically resizes
    as necessary, mirroring an array-based data structure.
    """

    def __init__(self) -> None:
        self._contacts: list[Contact] = []

    def add_contact(self, name: str, phone: str) -> None:
        """Add a new contact to the list."""
        self._contacts.append(Contact(name, phone))

    def search_contact(self, name: str) -> Optional[str]:
        """Return the phone number for the contact with the given name.

        If the contact is not found, returns None.
        """
        for contact in self._contacts:
            if contact.name == name:
                return contact.phone
        return None

    def delete_contact(self, name: str) -> bool:
        """Delete the contact with the given name.

        Returns True if a contact was removed, False otherwise.
        """
        for idx, contact in enumerate(self._contacts):
            if contact.name == name:
                # remove by index to avoid a second search
                del self._contacts[idx]
                return True
        return False

    def __repr__(self) -> str:
        return f"ArrayContactManager({self._contacts!r})"


# ----------------------------------------
# Linked list implementation
# ----------------------------------------

class Node:
    """Node for singly linked list containing a contact."""

    def __init__(self, contact: Contact, nxt: Optional[Node] = None) -> None:  # type: ignore
        self.contact = contact
        self.next = nxt

    def __repr__(self) -> str:
        return f"Node({self.contact!r}, next={self.next is not None})"


class LinkedListContactManager:
    """Contact manager using a singly linked list.

    The list grows dynamically as contacts are added.  Search and
    deletion operations traverse the list sequentially.  This
    implementation exposes the trade-offs of pointer-based structures
    vs. an array.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def add_contact(self, name: str, phone: str) -> None:
        """Insert a new contact at the front of the linked list."""
        new_node = Node(Contact(name, phone), self.head)
        self.head = new_node

    def search_contact(self, name: str) -> Optional[str]:
        """Search for a contact by name and return its phone number."""
        current = self.head
        while current is not None:
            if current.contact.name == name:
                return current.contact.phone
            current = current.next
        return None

    def delete_contact(self, name: str) -> bool:
        """Delete the first node whose contact matches the given name."""
        current = self.head
        prev: Optional[Node] = None
        while current is not None:
            if current.contact.name == name:
                if prev is None:
                    # removing head
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def __repr__(self) -> str:
        elems = []
        current = self.head
        while current is not None:
            elems.append(repr(current.contact))
            current = current.next
        return f"LinkedListContactManager([{', '.join(elems)}])"


# ----------------------------------------
# Efficiency comparison notes
# ----------------------------------------

# - Insertion efficiency:
#     * Array approach: append is amortized O(1); occasional resizing
#       may take O(n) but Python handles that under the hood.
#     * Linked list: always O(1) when inserting at the head (our
#       implementation).  No resizing cost, but each contact requires an
#       allocation for the node object.
# - Deletion efficiency:
#     * Array: O(n) to locate the contact and O(n) worst-case to shift
#       elements after removal (although Python's list `del` abstracts
#       this).  A deletion at the end is O(1) after locating.
#     * Linked list: O(n) to locate, but actual removal (pointer
#       adjustment) is O(1).  There is no shifting cost.  However,
#       finding the predecessor requires traversal.

# These comments can be expanded upon in a written report if required by
# the assignment.  The key differences revolve around contiguous memory
# vs. pointer-based flexibility and the costs of resizing/shifting.


# ----------------------------------------
# Demonstration / simple tests
# ----------------------------------------

def _demo(manager):
    print("Initial state:", manager)
    manager.add_contact("Alice", "555-1234")
    manager.add_contact("Bob", "555-5678")
    manager.add_contact("Charlie", "555-9012")
    print("After additions:", manager)
    print("Search for Bob:", manager.search_contact("Bob"))
    print("Delete Charlie:", manager.delete_contact("Charlie"))
    print("After deletion:", manager)
    print("Delete non-existent:", manager.delete_contact("Zoe"))


if __name__ == "__main__":
    print("=== Array based manager ===")
    arr_mgr = ArrayContactManager()
    _demo(arr_mgr)

    print("\n=== Linked list manager ===")
    ll_mgr = LinkedListContactManager()
    _demo(ll_mgr)
