import pytest


def test_tree_instance():
    bt = BinaryTree()
    assert bt


def test_TNode_instance():
    node = Node(tree1)
    tree = BinaryTree()
    assert node
    assert tree


def test_tree_commons(tree1, tree2):
    actual = tree_intersection(tree1, tree2)
    expected = [1, 13]
    assert actual == expected


def test_tree_no_commons(tree1, tree3):
    actual = tree_intersection(tree1, tree3)
    expected = []
    assert actual == expected


@pytest.fixture
def tree1():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(3)
    tree.root.right = Node(5)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(9)
    tree.root.right.left = Node(11)
    tree.root.right.right = Node(13)
    return tree


@pytest.fixture
def tree2():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(4)
    tree.root.right = Node(6)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(10)
    tree.root.right.left = Node(12)
    tree.root.right.right = Node(13)
    return tree


@pytest.fixture
def tree3():
    tree = BinaryTree()
    tree.root = Node(14)
    return tree
