from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Booking:
    ticket_id: str
    passenger_name: str
    train_number: str
    seat_number: str
    travel_date: str

    def travel_date_obj(self) -> datetime:
        return datetime.strptime(self.travel_date, '%Y-%m-%d')


def search_ticket_by_id(bookings: List[Booking], ticket_id: str) -> Optional[Booking]:
    """Return booking matching ticket_id, or None if not found."""
    for booking in bookings:
        if booking.ticket_id == ticket_id:
            return booking
    return None


def sort_bookings(bookings: List[Booking], key: str) -> List[Booking]:
    """Return a new list of bookings sorted by travelDate or seat_number."""
    if key == 'travelDate':
        return sorted(bookings, key=lambda b: b.travel_date_obj())
    if key == 'seat_number':
        return sorted(bookings, key=lambda b: int(''.join(filter(str.isdigit, b.seat_number))) if any(ch.isdigit() for ch in b.seat_number) else b.seat_number)
    raise ValueError("Sort key must be 'travelDate' or 'seat_number'")


if __name__ == '__main__':
    bookings = [
        Booking('T001', 'Alice', '123A', '12', '2026-05-20'),
        Booking('T002', 'Bob', '124B', '08', '2026-05-18'),
        Booking('T003', 'Charlie', '123A', '05', '2026-06-01'),
        Booking('T004', 'Dana', '125C', '15', '2026-05-18'),
    ]

    print('Search ticket T003:')
    found = search_ticket_by_id(bookings, 'T003')
    print(found)

    print('\nSort by travelDate:')
    for booking in sort_bookings(bookings, 'travelDate'):
        print(booking)

    print('\nSort by seat_number:')
    for booking in sort_bookings(bookings, 'seat_number'):
        print(booking)
