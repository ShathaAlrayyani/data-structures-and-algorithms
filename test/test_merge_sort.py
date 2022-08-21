from Algorithm.Sorting.merge_sort.merge_sort import *

def test_empty_array():
    actual = merge_sort([])
    assert actual == []

def test_positive_numbers():
    actual = merge_sort([5, 7, 9, 6, 1, 7, 4, 6])
    assert actual == [1, 4, 5, 6, 6, 7, 7, 9]

def test_negative_numbers():
    actual = merge_sort([-3, -2, -9, -7])
    assert actual == [-9, -7, -3, -2]

def test_mixed_numbers():
    actual = merge_sort([0, 5, 2, 7, 10, -2])
    assert actual == [-2, 0, 2, 5, 7, 10]

def test_reverse_sorted():
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    assert actual == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    assert actual == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    assert actual == [2, 3, 5, 7, 11, 13]