import pytest
from binary_tree.binary_tree import BinaryTree, Node
from binary_tree.binary_search_tree import BinarySearchTree


# Instantiate empty tree
def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None


# instantiate tree w/ single root node
def test_single_root_tree():
    tree = BinaryTree()
    tree.root = Node(25)
    assert tree.root.value == 25


# add left child and right child to single root node
def test_left_right_child_tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(2)
    tree.root.left = Node(3)
    assert tree.in_order() == [3, 1, 2]


# return collection from pre-order traversal
# visit - left - right
def test_bt_pre_order(tree):
    assert tree.pre_order() == [1, 3, 6, 15, 2, 4, 5]


# return collection from in-order traversal
# left - visit - right
def test_bt_in_order(tree):
    assert tree.in_order() == [6, 3, 15, 1, 4, 2, 5]


# return collection from post-order traversal
# left - right - visit
def test_bt_post_order(tree):
    assert tree.post_order() == [6, 15, 3, 4, 5, 2, 1]


# left - visit - right
def test_add_BST(bst):
    assert bst.in_order() == [5, 7, 9, 10, 15, 19]


def test_contains_BST_right(bst):
    assert bst.contains(19) is True
    assert bst.contains(5) is True


def test_contains_BST_left(bst):
    assert bst.contains(1) is False


@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(2)
    tree.root.left = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(15)
    return tree


@pytest.fixture
def bst():
    btree = BinarySearchTree()
    btree.add(10)
    btree.add(15)
    btree.add(7)
    btree.add(19)
    btree.add(9)
    btree.add(5)
    return btree
