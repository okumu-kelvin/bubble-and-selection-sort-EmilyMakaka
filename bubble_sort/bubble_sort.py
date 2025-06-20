def bubble_sort(unsorted_list):
    arr = unsorted_list.copy()
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped, the list is sorted
        if not swapped:
            break

    return arr


