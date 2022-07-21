from stack_and_queue.stack_and_queue import *


def fizz_buzz_tree(tree):
    """
    Determine whether the value of each node is divisible by 3, 5 or both.
    Create a new tree with the same structure as the original, but the values modified
    """
    root = Node(val)

    def _walk(val):

        new_tree = ''
        if val % 3 == 0:
            new_tree += 'Fizz'

        elif val % 5 == 0:
            new_tree += 'Buzz'
        elif val % 3 == 0 and val % 5 == 0:
            new_tree += 'FizzBuzz'
        else:
            new_tree += str(val)

    if not tree.root:
        return "The Tree is empty"
    new_tree = []
    qu = Queue()
    qu.enqueue(tree.root)
    pass

        # # A Tree node
        # class Node:
        #
        #     def __init__(self, d):
        #         self.data = d
        #         self.left = None
        #         self.right = None
        #
        # # Function to perform the Inorder
        # # traversal of the given tree
        # def display(root):
        #
        #     # Base Case
        #     if (root == None):
        #         return
        #
        #     # Recursively call for the
        #     # left subtree
        #     display(root.left)
        #
        #     # Print the value
        #     print(root.data, end=" ")
        #
        #     # Recursively call for the
        #     # right subtree
        #     display(root.right)
        #
        # # Function to convert the given tree
        # # to the multiplication tree
        # def convertTree(product, root):
        #
        #     # Base Case
        #     if (root == None):
        #         return
        #
        #     # Divide the total product by
        #     # the root's data
        #     root.data = product // (root.data)
        #
        #     # Go to the left subtree
        #     convertTree(product, root.left)
        #
        #     # Go to the right subtree
        #     convertTree(product, root.right)
