def bubble_sort(arr):
    # Get the number of elements in the list
    n = len(arr)

    # Repeat passes through the list until it is sorted
    for i in range(n):
        # Track whether any swaps occurred on this pass
        swapped = False

        # Compare each pair of adjacent elements in the unsorted portion
        for j in range(0, n - i - 1):
            # If the earlier element is larger, swap them to move the larger
            # element toward the end of the list.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps happened, the list is already sorted and we can stop.
        if not swapped:
            break


# Sample data to sort
data = [64, 34, 25, 12, 22, 11, 90]

# Sort the list using bubble sort
bubble_sort(data)

# Print the sorted result
print("Sorted array:", data)