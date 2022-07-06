import pytest
from binary_tree.binary_tree import Node, BinaryTree


# Instantiate empty tree
def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None


# instantiate tree w/ single root node
def test_single_root_tree():
    root_node = 25
    tree = BinaryTree()
    tree.root = Node(25)
    assert tree.root.value == root_node


# add left child and right child to single root node
def test_left_right_child_tree():
    tree = BinaryTree()
    one = Node(25)
    two = Node(12)
    three = Node(30)
    tree.root = one
    one.left = two
    one.right = three
    assert one.left and one.right
    expected = two and three


# return collection from preorder traversal
def test_bt_pre_order(test_tree):
    actual = test_tree.pre_order()
    expected = [1, 2, 4, 5, 3, 6]
    assert actual == expected


# return collection from inorder traversal
def test_bt_in_order(test_tree):
    actual = test_tree.in_order()
    expected = [4, 2, 5, 1, 6, 3]
    assert actual == expected


# return collection from postorder traversal
def test_bt_post_order(test_tree):
    actual = test_tree.post_order()
    expected = [4, 5, 2, 6, 3, 1]
    assert actual == expected


@pytest.fixture
def test_tree():
    tree = BinaryTree()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six

    return tree

#
# # Binary Search Tree
# def test_success_add_node_to_bst(test_bst):
#     test_bst.add(13)
#     test_bst.add(23)
#     assert test_bst.root.left.right.value == 13
#     assert test_bst.root.right.left.left.value == 23
#
#
# def test_success_bst_contains_value(test_bst):
#     print()
#     assert test_bst.contains(24) == True
#     assert test_bst.contains(60) == False
#     assert test_bst.contains(36) == True
#
#
# @pytest.fixture
# def test_bst():
#     bst = BinarySearchTree()
#     one = Node(15)
#     two = Node(12)
#     three = Node(25)
#     four = Node(24)
#     five = Node(29)
#     six = Node(36)
#     bst.root = one
#     one.left = two
#     one.right = three
#     three.left = four
#     three.right = five
#     five.right = six
#     return bst
