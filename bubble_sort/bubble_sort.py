def bubble_sort(unsorted_list):
    arr = unsorted_list.copy()  # Create a copy to avoid modifying the original list
    n = len(arr)

    for i in range(n):
        # Optimize by stopping if the list is already sorted
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr






