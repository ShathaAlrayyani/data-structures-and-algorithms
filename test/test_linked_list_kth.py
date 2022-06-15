import pytest
from linked_list.linked_list import LinkedList
"""Where k is greater than the length of the linked list
Where k and the length of the list are the same
Where k is not a positive integer
Where the linked list is of a size 1
“Happy Path” where k is not at the end, but somewhere in the middle of the linked list"""

def test_linked_list_kth():
    """
    Where k is greater than the length of the linked list
    """
    node = LinkedList()
    node.linked_list_kth(20)
    actual = node.head.value
    expected = 15
    assert actual == expected

def test_linked_list_kth1(node):
    """
    Where k and the length of the list are the same
    """
    node = LinkedList()
    node.linked_list_kth(10)
    actual = node.head.value
    expected = 15
    assert actual == expected


def test_linked_list_kth2(node):
    """
    Where k is not a positive integer
    """
    node = LinkedList()
    node.linked_list_kth(-2)
    actual = node.head.value
    expected = 15
    assert actual == expected

def test_linked_list_kth3(node):
    """
    Where the linked list is of a size 1
    """
    node = LinkedList()
    node.linked_list_kth(1)
    actual = node.head.value
    expected = 15
    assert actual == expected


def test_linked_list_kth4(node):
    """
    Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    """
    node = LinkedList()
    node.linked_list_kth(6)
    actual = node.head.value
    expected = 15
    assert actual == expected




