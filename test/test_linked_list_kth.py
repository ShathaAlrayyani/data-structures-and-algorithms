import pytest
from linked_list.linked_list import LinkedList


def test_linked_list_kth(node1):
    """
    Where k is greater than the length of the linked list
    """
    actual = node1.linked_list_kth(9)
    expected = 'This value is not found'
    assert expected == actual

def test_linked_list_kth1(node1):
    """
    Where k and the length of the list are the same
    """
    actual = node1.linked_list_kth(5)
    expected = 'This value is not found'
    assert expected == actual


def test_linked_list_kth2(node1):
    """
    Where k is not a positive integer
    """
    actual = node1.linked_list_kth(-2)
    expected = 'This value is not accepted'
    assert expected == actual


def test_linked_list_kth4(node1):
    """
    Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    """
    actual = node1.linked_list_kth(2)
    expected = 7
    assert expected == actual

def test_linked_list_kth5(node1):
    """
    Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    """
    actual = node1.linked_list_kth(4)
    expected = 0
    assert expected == actual


@pytest.fixture
def node1():
    node = LinkedList()
    node.append(0)
    node.append(12)
    node.append(7)
    node.append(13)
    node.append(15)
    return node


