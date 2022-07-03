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

def test_exists():
    assert PseudoQueue


def test_enqueue_single():
    pq = PseudoQueue()
    pq.enqueue(20)
    actual = pq.dequeue()
    expected = 20
    assert actual == expected


def test_dequeue_twenty(pq):
    actual = pq.dequeue()
    expected = 20
    assert actual == expected


def test_dequeue_fifteen(pq):
    pq.dequeue()
    actual = pq.dequeue()
    expected = 15
    assert actual == expected


@pytest.fixture
def pq():
    pq = PseudoQueue()
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    return pq

@pytest.fixture
def node2():
    node2 = PseudoQueue()
    node2.enqueue(1)
    node2.enqueue(3)
    node2.enqueue(5)
    node2.enqueue(7)
    node2.enqueue(9)
    return node2
