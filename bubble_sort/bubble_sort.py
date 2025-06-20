def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if _name_ == "_main_":
    test_array = [5, 4, 3, 2, 1, 0]
    sorted_array = bubble_sort(test_array)
    print("Sorted:", sorted_array)



