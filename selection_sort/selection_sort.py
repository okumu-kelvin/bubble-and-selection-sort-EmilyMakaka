def selection_sort(arr):
    result = arr[:]
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result

# Test cases
print(selection_sort([1, 2, 3]))  # Output: [1, 2, 3]
print(selection_sort([3, 2, 1]))  # Output: [1, 2, 3]
print(selection_sort([29, 10, 14, 37, 14]))  # Output: [10, 14, 14, 29, 37]


