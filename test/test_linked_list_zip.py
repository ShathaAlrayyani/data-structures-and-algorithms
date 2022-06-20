import pytest
from linked_list.linked_list import LinkedList

def test_linked_list_zip(node1, node2):
    node2.linked_list_zip(node2, node1)
    actual = node2.to_string()
    expected = '{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 9 } -> None'
    assert expected == actual

def test_linked_list_zip_empty(node1):
    node2 = LinkedList()
    actual = node2.linked_list_zip(node2, node1)
    expected = False
    assert expected == actual


def test_linked_list_zip_1st_longer():
    node = LinkedList()
    node.insert(5)
    node.insert(3)
    node.insert(1)
    node2 = LinkedList()
    node2.append(0)
    node2.append(2)
    node.linked_list_zip(node, node2)
    actual = node.to_string()
    expected = '{ 1 } -> { 0 } -> { 3 } -> { 2 } -> { 5 } -> None'
    assert expected == actual


def test_linked_list_zip_1st_shorter():
    node = LinkedList()
    node.append(1)
    node.append(3)
    node2 = LinkedList()
    node2.append(0)
    node2.append(2)
    node2.append(5)
    node2.append(7)
    node2.linked_list_zip(node, node2)
    actual = node.to_string()
    expected = '{ 1 } -> { 0 } -> { 3 } -> { 2 } -> { 5 } -> { 7 } -> None'
    assert expected == actual

@pytest.fixture
def node1():
    node = LinkedList()
    node.insert(5)
    node.insert(3)
    node.insert(1)
    node.append(7)
    node.append(9)
    return node


@pytest.fixture
def node2():
    node2 = LinkedList()
    node2.append(0)
    node2.append(2)
    node2.append(4)
    node2.append(6)
    node2.append(8)
    return node2
