# Collection of sorting algorithms


def bubblesort(my_list):

    # don't modify the original list
    my_list_c = my_list.copy()

    for i in range(0, len(my_list_c) - 1):
        for j in range(0, len(my_list_c) - 1 - i):
            if my_list_c[j] > my_list_c[j+1]:
                my_list_c[j], my_list_c[j+1] = my_list_c[j+1], my_list_c[j]
    return my_list_c


def mergesort(my_list):
    # recursive algorithm that splits a list into separate lists of size 1 and then merges those back together

    my_list_c = my_list.copy()
    if len(my_list_c) > 1:
        mergesort_impl(my_list_c)

    return my_list_c


def mergesort_impl(a_list):
    # split the list
    if len(a_list) > 1:
        middle = len(a_list)//2
        left = a_list[:middle]
        right = a_list[middle:]

        # run merge sort on each half
        mergesort_impl(left)
        mergesort_impl(right)

        # append the large value to compare lesser values with
        left.append(999999999)
        right.append(999999999)

        i = 0
        j = 0
        for k in range(0, len(left) + len(right)-2):
            if left[i] >= right[j]:
                a_list[k] = right[j]
                j += 1
            else:
                a_list[k] = left[i]
                i += 1


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


# This code is contributed by Mohit Kumra


def quicksort(my_list):
    my_list_c = my_list.copy()

    quickSort(my_list_c, 0, len(my_list_c)-1)
    return my_list_c

def builtinsort(my_list):
    return sorted(my_list)


my_list = [4, 1, 3, 8, 0]
ordered_list = quicksort(my_list)

print(ordered_list)