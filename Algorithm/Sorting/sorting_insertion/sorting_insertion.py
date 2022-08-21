def sorting_insertion(lst):
    """
    this function will take an array of integers and return it in sorted order
    """
    if len(lst) == 0:
        return 'This Array is EMPTY!'
    elif len(lst) == 1:
        return lst
    else:
        for i in range(len(lst)):
            j = i - 1
            temp = lst[i]
            while j >= 0 and temp < lst[j]:
                lst[j + 1] = lst[j]
                j = j - 1
            lst[j + 1] = temp
        return lst


if __name__ == "__main__":
    print(sorting_insertion([]))  # return this array is empty!
    print(sorting_insertion([3]))  # returns 3
    print(sorting_insertion([4, 6, 2, 5, 10]))

