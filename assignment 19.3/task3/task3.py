def bubble_sort(lst):
    """
    Sorts a list in ascending order using the bubble sort algorithm.
    """
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap the elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

# Example usage
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    sorted_list = bubble_sort(sample_list)
    print("Sorted list:", sorted_list)
