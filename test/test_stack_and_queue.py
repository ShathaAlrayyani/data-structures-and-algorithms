import pytest
from DS.stack_queue.stack_and_queue.stack_and_queue import Stack, Queue


def test_Stack_push(node1):
    actual = node1.__str__()
    expected = '86420'
    assert expected == actual

def test_Stack_pop(node1):
    actual = node1.pop()
    expected = 8
    assert expected == actual

def test_Stack_pop_str(node1):
    node1.pop()
    actual = node1.__str__()
    expected = '6420'
    assert expected == actual

def test_Stack_pop_empty():
    node = Stack()
    with pytest.raises(Exception) as erorr:
        node.peek()
    assert str(erorr.value) == "the list is empty"

def test_Stack_peek(node1):
    actual = node1.peek()
    expected = 8
    assert expected == actual

def test_Stack_peek_empty():
    node = Stack()
    with pytest.raises(Exception) as erorr:
        node.peek()
    assert str(erorr.value) == "the list is empty"

def test_Stack_is_empty(node1):
    actual = node1.is_empty()
    expected = False
    assert expected == actual

def test_Queue_enqueue(node2):
    actual = node2.__str__()
    expected = '13579'
    assert expected == actual

def test_Queue_dequeue(node2):
    actual = node2.dequeue()
    expected = 1
    assert expected == actual

def test_Queue_dequeue_str(node2):
    node2.dequeue()
    actual = node2.__str__()
    expected = '3579'
    assert expected == actual

def test_Queue_dequeue_empty():
    node = Queue()
    with pytest.raises(Exception) as erorr:
        node.dequeue()
    assert str(erorr.value) == "the list is empty"


def test_Queue_peek(node2):
    actual = node2.peek()
    expected = 1
    assert expected == actual

def test_Queue_peek_empty():
    node = Queue()
    with pytest.raises(Exception) as erorr:
        node.peek()
    assert str(erorr.value) == "the list is empty"

def test_Queue_is_empty(node2):
    actual = node2.is_empty()
    expected = False
    assert expected == actual

@pytest.fixture
def node1():
    node = Stack()
    node.push(0)
    node.push(2)
    node.push(4)
    node.push(6)
    node.push(8)
    return node


@pytest.fixture
def node2():
    node2 = Queue()
    node2.enqueue(1)
    node2.enqueue(3)
    node2.enqueue(5)
    node2.enqueue(7)
    node2.enqueue(9)
    return node2

