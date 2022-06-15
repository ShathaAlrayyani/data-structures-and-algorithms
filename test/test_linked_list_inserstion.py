import pytest
from linked_list.linked_list import LinkedList


def test_str_append(node1):
    """
    return a collection of all the values that exist in the linked list
    to make sure append method Can successfully add multiple nodes to the end of a linked list
    """
    actual = node1.to_string()
    expected = '{ 0 } -> { 12 } -> { 7 } -> { 13 } -> { 15 } -> None'
    assert actual == expected


@pytest.mark.skip(reason="I didn't finish the function yet")
def test_str_insert_before(node1):
    """
    return a collection of all the values that exist in the linked list
    to make sure append method Can successfully add multiple nodes to the end of a linked list
    """
    actual = node1.to_string()
    expected = '{ 0 } -> { 12 } -> { 7 } -> { 13 } -> { 15 } -> None'
    assert actual == expected

@pytest.mark.skip(reason="I didn't finish the function yet")
def test_str_insert_after(node1):
    """
    return a collection of all the values that exist in the linked list
    to make sure append method Can successfully add multiple nodes to the end of a linked list
    """
    actual = node1.to_string()
    expected = '{ 0 } -> { 12 } -> { 7 } -> { 13 } -> { 15 } -> None'
    assert actual == expected


def test_append(node1):
    """
  Can successfully add a node to the end of the linked list

    """
    actual = node1.head.value
    expected = 0
    assert expected == actual

@pytest.mark.skip(reason="I didn't finish the function yet")
def test_insert_before1(node):
    """
  Can successfully insert a node before a node located i the middle of a linked list
    """
    actual = node.head.value
    expected = 22
    assert expected == actual
    actual = node.head.value
    expected = 0
    assert expected == actual

@pytest.mark.skip(reason="I didn't finish the function yet")
def test_insert_before2(node):
    """
  Can successfully insert a node before the first node of a linked list
    """
    actual = node.head.value
    expected = 9
    assert expected == actual
    actual = node.head.next
    expected = 7
    assert expected == actual


@pytest.mark.skip(reason="I didn't finish the function yet")
def test_insert_after1(node):
    """
 Can successfully insert after a node in the middle of the linked lis
    """
    actual = node.head.value
    expected = 0
    assert expected == actual


@pytest.mark.skip(reason="I didn't finish the function yet")
def test_insert_after2(node):
    """
  Can successfully insert a node after the last node of the linked list
    """
    actual = node.head.value
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
#
#
# @pytest.fixture
# def linked_list():
#     node = LinkedList()
#     node.insert_before(7, 9)
#     node.insert_before(0, 22)
# #     node.insert_before(7, 5)
# #     node.insert_before(7, 5)
# #     node.insert_before(7, 5)
# #     node.insert_after(7, 5)
# #     return node
