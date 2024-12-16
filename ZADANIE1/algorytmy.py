from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3




def merge_sort(array: MonitorowanaTablica, left=None, right=None):
# twoj kod
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    middle = (left + right) // 2
    merge_sort(array, left, middle)
    merge_sort(array, middle + 1, right)
    merge(array, left, middle, right)


def merge(array: MonitorowanaTablica, left, middle, right):
    """Merges two sorted subarrays."""
    # twoj kod, moze sie przydac
    merged = []
    left_index = left
    right_index = middle + 1

    while left_index <= middle or right_index <= right:
        if left_index > middle:
            merged.append(array[right_index])
            right_index += 1
        elif right_index > right:
            merged.append(array[left_index])
            left_index += 1
        elif array[left_index] <= array[right_index]:
            merged.append(array[left_index])
            left_index += 1
        else:
            merged.append(array[right_index])
            right_index += 1

    for idx in range(len(merged)):
        array[left + idx] = merged[idx]


def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    """Performs quick sort on the given array."""
    # twoj kod
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    pivot = partition(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)


def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""
    # twoj kod, moze sie przydac
    pivot_value = array[right]
    partition_index = left

    for current_index in range(left, right):
        if array[current_index] <= pivot_value:
            array[partition_index], array[current_index] = array[current_index], array[partition_index]
            partition_index += 1

    array[partition_index], array[right] = array[right], array[partition_index]
    return partition_index


def tim_sort(array: MonitorowanaTablica):
# twoj kod
    min_run = 32
    length = len(array)

    for start in range(0, length, min_run):
        end = min(start + min_run - 1, length - 1)
        insertion_sort(array, start, end)

    size = min_run

    while size < length:
        for left in range(0, length, size * 2):
            middle = left + size - 1
            right = min(left + size * 2 - 1, length - 1)
            merge(array, left, middle, right)

        size *= 2



algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]

