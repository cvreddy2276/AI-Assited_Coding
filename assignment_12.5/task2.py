def binary_Search(arr, target):
    """Return the index of target in sorted arr using binary search.

    Parameters:
        arr (list): Sorted list of comparable elements.
        target: Value to search for in arr.

    Returns:
        int: Index of target if found, otherwise -1.

    Complexity:
        Best case: O(1) when target is found at the middle.
        Average case: O(log n) because the search space halves each step.
        Worst case: O(log n) when target is not present or found at an extreme.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    tests = [
        ([], 5),
        ([1], 1),
        ([1], 2),
        ([1, 3, 5, 7, 9], 7),
        ([1, 3, 5, 7, 9], 2),
        ([2, 4, 6, 8, 10], 10),
        ([2, 4, 6, 8, 10], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ]

    for arr, target in tests:
        result = binary_Search(arr, target)
        print(f'arr={arr}, target={target} -> index={result}')
