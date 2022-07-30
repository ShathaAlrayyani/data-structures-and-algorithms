""" This Function should reverse any array """
def reverse(lst):
    if len(lst) == 1:
        return lst
    return reverse(lst[1:]) + lst[0:1]


list1 = [1, 22, 3, 44, 5]

print(reverse(list1))
