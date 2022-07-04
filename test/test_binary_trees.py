import pytest
from binary_tree.binary_tree import TreeNode, BinaryTree,BinarySearchTree


# Instantiate empty tree
def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None


# instantiate tree w/ single root node
def test_single_root_tree():
    root_node = 25
    tree = BinaryTree(TreeNode)
    assert tree.root == root_node


# add left child and right child to single root node
def test_left_right_child_tree():
    tree = BinaryTree()
    one = TreeNode(25)
    two = TreeNode(12)
    three = TreeNode(30)
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
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six

    return tree


# Binary Search Tree
def test_success_add_node_to_bst(test_bst):
    test_bst.add(13)
    test_bst.add(23)
    assert test_bst.root.left.right.value == 13
    assert test_bst.root.right.left.left.value == 23


def test_success_bst_contains_value(test_bst):
    print()
    assert test_bst.contains(24) == True
    assert test_bst.contains(60) == False
    assert test_bst.contains(36) == True


@pytest.fixture
def test_bst():
    bst = BinarySearchTree()
    one = TreeNode(15)
    two = TreeNode(12)
    three = TreeNode(25)
    four = TreeNode(24)
    five = TreeNode(29)
    six = TreeNode(36)
    bst.root = one
    one.left = two
    one.right = three
    three.left = four
    three.right = five
    five.right = six
    return bst