def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the current position holds the minimum element
        min_idx = i

        # Iterate through the unsorted portion to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
