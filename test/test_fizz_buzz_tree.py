import pytest
from DS.Trees.fizz_buzz_tree.fizz_buzz_tree import *
# from DS.Trees.fizz_buzz_tree.k_ary_tree import *


def test_fizz_buzz_tree(tree):
    actual = fizz_buzz_tree(tree)
    assert actual == ['Buzz', '7', 'FizzBuzz', '8', 'Buzz']


def test_empty_tree():
    tree = KaryTrees()
    actual = fizz_buzz_tree(tree.level_order())
    assert actual == "The Tree is empty"


# instantiate tree w/ single root node
def test_single_root_tree():
    t = KaryTrees()
    one = Node(15)
    t.root = one
    actual = fizz_buzz_tree(t.level_order())
    assert actual == ['FizzBuzz']


@pytest.fixture
def tree():
    tree = KaryTrees()
    on = Node(5)
    tree.root = on
    two = Node(7)
    three = Node(15)
    four = Node(8)
    five = Node(95)
    on.children.append(two)
    on.children.append(three)
    on.children.append(four)
    two.children.append(five)
    print(tree)
    return tree.level_order()
