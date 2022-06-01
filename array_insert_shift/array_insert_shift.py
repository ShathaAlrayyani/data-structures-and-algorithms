""" This function should return an array
with the new value added at the middle index."""
def insertShiftArray(lst, num):
    n = len(lst) // 2
    lst.insert(n, num)
    return print(lst)


""" This function should return an array 
without the value at the middle index."""
def deleteShiftArray(arr):
    n = len(arr) // 2
    arr.pop(n)
    print(arr)


lst1 = [3, 6, 12, 7, 2]
lst2 = [1, 7, 13, 77, 22, 9,10]

insertShiftArray([3, 5, 2, 17 , 24,13,1] , "banda" )

deleteShiftArray([3, 5, 2, 17 , 24,13,1] )
