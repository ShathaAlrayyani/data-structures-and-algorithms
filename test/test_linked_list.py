import pytest
from linked_list.linked_list import LinkedList


#  instantiate an empty linked list
def test_linked_list(node):
    assert node


def test_head(node):
    """
    check the first node is the Head
    Can properly insert into the linked list
    :param node:
    :return: None
    """
    actual = node.head.value
    expected = 0
    assert actual == expected


def test_insert(node):
    """
  insert into the linked list
  The head property will properly point to the first node in the linked list
    :param node:
    :return: None
    """
    actual = node.head.value
    expected = 0
    assert expected == actual

def test_not_inc(node):
    """
   Will return false when searching for a value in the linked list that does not exist
    :param LinkedList:
    :return: False
    """
    actual = node.include(45)
    expected = False
    assert actual == expected


def test_include(node):
    """
    Will return true when finding a value within the linked list that exists
    """
    actual = node.include(12)
    expected = True
    assert actual == expected



def test_str(node):
    '''
    return a collection of all the values that exist in the linked list
    '''
    actual = node.to_string()
    expected = '{ 0 } -> { 12 } -> { 7 } -> { 13 } -> { 15 } -> None'
    assert actual == expected



@pytest.fixture
def ll():
    node = LinkedList()
    node.insert(0)
    node.insert(12)
    node.insert(7)
    node.insert(13)
    node.insert(15)
    return node
