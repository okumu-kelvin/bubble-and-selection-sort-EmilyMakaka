def bubble_sort(unsorted_list):
    arr = unsorted_list.copy()  # Create a copy to avoid modifying the original list
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

# Test cases
def test_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert bubble_sort([4, 5, 3, 4]) == [3, 4, 4, 5]

test_sorted()
test_reverse()
test_duplicates()



