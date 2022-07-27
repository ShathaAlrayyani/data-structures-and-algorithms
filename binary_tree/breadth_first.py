from binary_tree import *
from stack_and_queue.stack_and_queue import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first(tree):
    """This function Traverse the input tr using a Breadth-first approach"""
    if not tree.root:
        return "The Tree is empty"
    output = []
    queue = Queue()
    queue.enqueue(tree.root)
    while not queue.is_empty():
        front = queue.dequeue()
        output.append(front.value)
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
    return output


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(15)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.left.right = Node(95)

    print(breadth_first(tree))