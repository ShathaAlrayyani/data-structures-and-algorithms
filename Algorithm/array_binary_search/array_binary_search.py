def BinarySearch(lst, key):
    s = 0
    y = len(lst) - 1
    while y >= s:
        m = (s + y) // 2
        if lst[m] == key:
            return m
        elif lst[m] < key:
            s = m + 1
        elif lst[m] > key:
            y = m - 1

    return -1


BinarySearch([1, 2, 3, 4, 5, 6, 7, 8], 6)
