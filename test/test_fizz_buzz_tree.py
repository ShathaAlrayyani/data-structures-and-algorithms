import pytest
from fizz_buzz_tree.fizz_buzz_tree import *
from binary_tree.binary_tree import *


def test_fizz_buzz_tree(tree):
    assert fizz_buzz_tree(tree) == ['FizzBuzz', 7, 1, 'Fizz', 'Buzz', 7, 92]


def test_empty_tree():
    tree = BinaryTree()
    assert fizz_buzz_tree(tree) == "The Tree is empty"


# instantiate tree w/ single root node
def test_single_root_tree():
    t = BinaryTree()
    t.root = Node(15)
    assert fizz_buzz_tree(t) == '15'


@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(15)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.left.right = Node(95)
    tree.root.right.left = Node(7)
    tree.root.right.right = Node(92)
    return tree
