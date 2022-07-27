import pytest

from binary_tree.binary_tree import *
from binary_tree.breadth_first import breadth_first


# Instantiate empty tr
def test_empty_tree():
    tree = BinaryTree()
    assert breadth_first(tree) == "The Tree is empty"


# instantiate tr w/ single root node
def test_single_root_tree():
    t = BinaryTree()
    t.root = Node(15)
    assert breadth_first(t) == [15]


def test_tree(tree):
    assert breadth_first(tree) == [15, 7, 1, 9, 95, 7, 92]

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

