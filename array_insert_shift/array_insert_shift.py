"""This function for adding a new value
 in the middle index of a list"""
def insertShiftArray(lst,num):
    n = len(lst) // 2
    if len(lst) % 2 != 0:
        n = n + 1
    lst.insert(n,num)
    print(lst)


"""This function for deleting the value
 in the middle index of a list"""
def deleteShiftArray(lst):
    n = len(lst) // 2
    lst.pop(n)
    print(lst)


insertShiftArray([1,2,3,4,5],6)
deleteShiftArray([1,2,3,4,5])