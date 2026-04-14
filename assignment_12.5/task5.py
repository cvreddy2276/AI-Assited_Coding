from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Allocation:
    student_id: str
    room_number: str
    floor: int
    allocation_date: str

    def allocation_date_obj(self) -> datetime:
        return datetime.strptime(self.allocation_date, '%Y-%m-%d')


def search_allocation_by_student_id(allocations: List[Allocation], student_id: str) -> Optional[Allocation]:
    """Search allocation details by student ID.

    Best optimized approach: use a dictionary mapping student IDs to allocations for O(1) lookup.
    If the input list is unsorted, a linear scan is O(n).
    If the list is pre-sorted by student_id, binary search is O(log n).
    """
    for allocation in allocations:
        if allocation.student_id == student_id:
            return allocation
    return None


def sort_allocations(allocations: List[Allocation], key: str) -> List[Allocation]:
    """Return allocations sorted by room_number or allocation_date.

    Uses Python's Timsort, which runs in O(n log n) time.
    """
    if key == 'room_number':
        return sorted(allocations, key=lambda a: int(''.join(filter(str.isdigit, a.room_number))) if any(ch.isdigit() for ch in a.room_number) else a.room_number)
    if key == 'allocation_date':
        return sorted(allocations, key=lambda a: a.allocation_date_obj())
    raise ValueError("Sort key must be 'room_number' or 'allocation_date'")


if __name__ == '__main__':
    allocations = [
        Allocation('S001', '101A', 1, '2026-07-01'),
        Allocation('S002', '102B', 1, '2026-06-28'),
        Allocation('S003', '201A', 2, '2026-07-03'),
        Allocation('S004', '103C', 1, '2026-06-30'),
    ]

    print('Search allocation for S003:')
    print(search_allocation_by_student_id(allocations, 'S003'))

    print('\nSort by room_number:')
    for allocation in sort_allocations(allocations, 'room_number'):
        print(allocation)

    print('\nSort by allocation_date:')
    for allocation in sort_allocations(allocations, 'allocation_date'):
        print(allocation)
