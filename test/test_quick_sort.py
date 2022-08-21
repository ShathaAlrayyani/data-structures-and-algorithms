import pytest
from Algorithm.Sorting.quick_sort.quick_sort import *

def test_positive_numbers():
    a = [5, 7, 9, 6, 1, 7, 4, 6]
    quick_sort(a, 0, 7)
    actual = a
    assert actual == [1, 4, 5, 6, 6, 7, 7, 9]

def test_negative_numbers():
    b = [-3, -2, -9, -7]
    quick_sort(b, 0, 3)
    actual = b
    assert actual == [-9, -7, -3, -2]

def test_mixed_numbers():
    c = [0, 5, 2, 7, 10, -2]
    quick_sort(c, 0, 5)
    actual = c
    assert actual == [-2, 0, 2, 5, 7, 10]

def test_reverse_sorted():
    d = [20, 18, 12, 8, 5, 2, -2]
    quick_sort(d, 0, 6)
    actual = d
    assert actual == [-2, 2, 5, 8, 12, 18, 20]

def test_few_uniques():
    e = [5, 12, 7, 5, 5, 7]
    quick_sort(e, 0, 5)
    actual = e
    assert actual == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    f = [2, 3, 5, 7, 13, 11]
    quick_sort(f, 0, 5)
    actual = f
    assert actual == [2, 3, 5, 7, 11, 13]