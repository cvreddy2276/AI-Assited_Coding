def quicksort(arr):
    """Sort a list using the quick sort algorithm.

    The function returns a new list in ascending order.
    It uses the middle element as the pivot and partitions the list into
    elements less than, equal to, and greater than the pivot.

    Args:
        arr: A list of comparable values.

    Returns:
        A new sorted list containing the same values as ``arr``.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def merge_sort(arr):
    """Sort a list using the merge sort algorithm.

    The function returns a new list in ascending order. It splits the input
    list recursively and then merges the sorted halves.

    Args:
        arr: A list of comparable values.

    Returns:
        A new sorted list containing the same values as ``arr``.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted lists into a single sorted list.

    Args:
        left: A sorted list.
        right: A sorted list.

    Returns:
        A new sorted list containing all values from ``left`` and ``right``.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def measure_sort_time(sort_fn, arr):
    """Measure the execution time of a sorting function."""
    import time

    start = time.perf_counter()
    sorted_arr = sort_fn(arr)
    end = time.perf_counter()
    return sorted_arr, end - start


def compare_algorithms(size=1000):
    """Compare quicksort and merge sort on random, sorted, and reverse-sorted lists."""
    import random

    inputs = {
        "random": [random.randint(0, size) for _ in range(size)],
        "sorted": list(range(size)),
        "reverse-sorted": list(range(size, 0, -1)),
    }

    print("\nComparison of sorting algorithms:")
    print(f"{'Input type':<15}{'Quick Sort time (s)':>22}{'Merge Sort time (s)':>22}")

    for label, values in inputs.items():
        quick_sorted, quick_time = measure_sort_time(quicksort, values)
        merge_sorted, merge_time = measure_sort_time(merge_sort, values)

        # Verify both algorithms produce the same result and the result is sorted.
        assert quick_sorted == merge_sorted == sorted(values)

        print(f"{label:<15}{quick_time:>22.6f}{merge_time:>22.6f}")


if __name__ == "__main__":
    sample_data = [33, 10, 55, 71, 29, 8, 90]
    print("Original list:", sample_data)

    sorted_with_quick = quicksort(sample_data)
    print("Quick sort result:", sorted_with_quick)

    sorted_with_merge = merge_sort(sample_data)
    print("Merge sort result:", sorted_with_merge)

    compare_algorithms(size=2000)
