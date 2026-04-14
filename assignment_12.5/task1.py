def merge_sort(arr):
    """Sort and return a new list using merge sort."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == '__main__':
    sample = [38, 27, 43, 3, 9, 82, 10]
    print('Original:', sample)
    print('Sorted:  ', merge_sort(sample))
