def selection_sort(arr):

    result = arr[:]  # Make a copy to avoid modifying the input
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                 min_index = j
        result[i], result[min_index] = result[min_index], result[i]
        return result

