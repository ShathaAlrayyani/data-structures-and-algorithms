"""This function for adding a new value
 in the middle index of a list"""
def insertShiftArray(lst, num):
    n = len(lst) // 2
    if len(lst) % 2 != 0:
        n = n + 1
        new_list = lst[:n] + [num] + lst[n:]
    else:
        new_list = lst[:n] + [num] + lst[n:]
    print(new_list)


"""This function for deleting the value
 in the middle index of a list"""
def deleteShiftArray(lst):
    n = len(lst) // 2
    new_list = lst[:n] + lst[n+1:]
    print(new_list)


insertShiftArray([1,2,3,4,5],6)
deleteShiftArray([1,2,3,4,5])

""" n = len(lst) // 2
    new_list = []
    list_len = len(lst)
    i = 0
    for x in lst:
        if list_len % 2 != 0:
            n = (len(lst) // 2) + 1
            if i < n:
                new_list.append(x)
                i += 1
            elif i == n:
                new_list.append(num)
                new_list.append(x)
                i += 1
            elif i > n:
                new_list.append(x)
                i += 1
        else:
            if i < n:
                new_list.append(x)
                i += 1
            elif i == n:
                new_list.append(num)
                new_list.append(x)
                i += 1
            elif i > n:
                new_list.append(x)
                i += 1
    print(new_list)"""