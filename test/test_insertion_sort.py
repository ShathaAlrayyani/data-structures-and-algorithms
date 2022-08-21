from Algorithm.Sorting.sorting_insertion.sorting_insertion import sorting_insertion


def test_empty_array():
    """
    this function test an empty array ( the length of the array equals zero )
    """
    actual = sorting_insertion([])
    assert actual == 'This Array is EMPTY!'


def test_one_element_array():
    """
    this function test one element array ( the length of the array equals 1 )
    """
    actual = sorting_insertion([7])
    assert actual == [7]

def test_array_positive_int():
    """
    this function test an array ( the length of the array equals n )
    """
    actual = sorting_insertion([7, 3, 5, 10, 1])
    assert actual == [1, 3, 5, 7, 10]

def test_array_negative_ing():
    """
    his function test an array contains negative int ( the length of the array equals n )
    """
    actual = sorting_insertion([7, -3, 5, 10, 1])
    assert actual == [-3, 1, 5, 7, 10]


def test_nearly_sorted_array():
    """
    this function test an array of nearly sorted array
    """
    actual = sorting_insertion([1, 3, 4, 6, 15, 10])
    assert actual == [1, 3, 4, 6, 10, 15]



