import random
import sys
import time
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    name: str
    roll: str
    cgpa: float


def print_students(students: List[Student]) -> None:
    print("\nSorted Student Records:")
    print(f"{'Name':<25}{'Roll Number':<15}{'CGPA':<6}")
    for student in students:
        print(f"{student.name:<25}{student.roll:<15}{student.cgpa:.2f}")


def print_top_students(students: List[Student], top_n: int = 3) -> None:
    print(f"\nTop {min(top_n, len(students))} Performer{'s' if top_n != 1 else ''}:")
    print(f"{'Name':<25}{'Roll Number':<15}{'CGPA':<6}")
    for student in students[:top_n]:
        print(f"{student.name:<25}{student.roll:<15}{student.cgpa:.2f}")


def quick_sort(students: List[Student], low: int, high: int) -> None:
    if low < high:
        pivot_index = partition(students, low, high)
        quick_sort(students, low, pivot_index - 1)
        quick_sort(students, pivot_index + 1, high)


def partition(students: List[Student], low: int, high: int) -> int:
    pivot = students[high].cgpa
    i = low - 1
    for j in range(low, high):
        if students[j].cgpa >= pivot:
            i += 1
            students[i], students[j] = students[j], students[i]
    students[i + 1], students[high] = students[high], students[i + 1]
    return i + 1


def merge_sort(students: List[Student]) -> List[Student]:
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])
    return merge(left, right)


def merge(left: List[Student], right: List[Student]) -> List[Student]:
    merged: List[Student] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].cgpa >= right[j].cgpa:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def generate_random_students(n: int) -> List[Student]:
    return [
        Student(name=f"Student{i+1}", roll=f"R{i+1:05d}", cgpa=random.uniform(0.0, 10.0))
        for i in range(n)
    ]


def benchmark_sort(students: List[Student], sort_func, *, in_place: bool) -> float:
    data = students.copy()
    start = time.perf_counter()
    if in_place:
        sort_func(data, 0, len(data) - 1)
    else:
        sort_func(data)
    return time.perf_counter() - start


def run_benchmarks() -> None:
    sys.setrecursionlimit(100000)
    sizes = [5000, 10000, 20000]
    print("\nBenchmarking sort performance for large datasets (descending CGPA)...")
    print(f"{'N':>8} {'Quick Sort (s)':>18} {'Merge Sort (s)':>18}")
    for n in sizes:
        students = generate_random_students(n)
        quick_time = benchmark_sort(students, quick_sort, in_place=True)
        merge_time = benchmark_sort(students, merge_sort, in_place=False)
        print(f"{n:>8} {quick_time:>18.4f} {merge_time:>18.4f}")
    print("\nNote: results vary by system load and Python interpreter.")


def read_students() -> List[Student]:
    while True:
        try:
            n = int(input("Enter the number of students: ").strip())
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    students = []
    for i in range(1, n + 1):
        print(f"\nEnter details for student {i}:")
        name = input("Name: ").strip()
        roll = input("Roll Number: ").strip()
        while True:
            try:
                cgpa = float(input("CGPA: ").strip())
                break
            except ValueError:
                print("Please enter a valid CGPA.")
        students.append(Student(name=name, roll=roll, cgpa=cgpa))

    return students


def main() -> None:
    students = read_students()

    print("\nSelect sorting algorithm:")
    print("1. Quick Sort")
    print("2. Merge Sort")
    print("3. Benchmark performance on large random datasets")

    choice = input("Enter choice (1, 2, or 3): ").strip()

    if choice == "1":
        sorted_students = students.copy()
        quick_sort(sorted_students, 0, len(sorted_students) - 1)
        print_students(sorted_students)
        print_top_students(sorted_students)
    elif choice == "2":
        sorted_students = merge_sort(students)
        print_students(sorted_students)
        print_top_students(sorted_students)
    elif choice == "3":
        run_benchmarks()
    else:
        print("Invalid choice. Please run the program again and choose 1, 2, or 3.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--benchmark":
        run_benchmarks()
    else:
        main()
