def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n):
        swapped = False


        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap elements
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # If no elements were swapped, the list is sorted
        if not swapped:
            break

    return unsorted_list