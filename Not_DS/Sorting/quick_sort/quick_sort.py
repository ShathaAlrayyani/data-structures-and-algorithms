def quick_sort(arr, Left, Right):
    if Left < Right:
        p = partition(arr, Left, Right)
        # Sort the left side
        quick_sort(arr, Left, p-1)
        # Sort the right side
        quick_sort(arr, p+1, Right)



def partition(arr, Left, Right):
    pivot = arr[Right]
    low = Left - 1
    for i in range(Left, Right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)
    swap(arr, Right, low + 1)
    return low + 1


def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


if __name__ == "__main__":
    print('*' * 50)
    a = [8, 4, 23, 42, 16, 15]
    quick_sort(a, 0, 5)
    print(a)
    print('*' * 50)
    # Reverse-sorted
    dana = [20, 18, 12, 8, 5, -2]
    quick_sort(dana, 0, 5)
    print(dana)
    print('*' * 50)


