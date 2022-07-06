import pytest
from fizz_buzz_tree.fizz_buzz_tree import *
from binary_tree.binary_tree import *


# If the value is divisible by 3, replace the value with “Fizz”
# If the value is divisible by 5, replace the value with “Buzz”
# If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
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



"""If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String."""




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
