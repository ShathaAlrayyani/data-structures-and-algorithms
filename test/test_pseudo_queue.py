import pytest
from pseudo_queue.pseudo_queue import PseudoQueue


def test_pseudo_queue_dequeue(node2):
    actual = node2.dequeue()
    expected = 1
    assert actual == expected

def test_pseudo_queue_dequeue1(node2):
    node2.dequeue()
    actual = node2.dequeue()
    expected = 3
    assert actual == expected


def test_Queue_enqueue(node2):
    actual = node2.__str__()
    expected = '9\n7\n5\n3\n1\n'
    assert expected == actual

@pytest.fixture
def node2():
    node2 = PseudoQueue()
    node2.enqueue(1)
    node2.enqueue(3)
    node2.enqueue(5)
    node2.enqueue(7)
    node2.enqueue(9)
    return node2
