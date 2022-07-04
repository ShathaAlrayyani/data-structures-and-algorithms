from stack_and_queue.stack_and_queue import *


class EmptyQueueException(Exception):
    pass


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        if not self.root:
            return self.root

        def _walk(root):
            print(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)

    def in_order(self):
        if not self.root:
            return self.root

        def _walk(root):

            if root.left:
                _walk(root.left)

            print(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)

    def post_order(self):
        if not self.root:
            return self.root

        def _walk(root):

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            print(root.value)

        _walk(self.root)


class BinarySearchTree:
    def add(self):
        """add new value to the tree"""
        pass
    def contains(self):
        """return true if the value I'm looking for exist else return False"""
        pass


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = TreeNode(10)
    tree.root.left = TreeNode(20)
    tree.root.right = TreeNode(50)
    tree.root.left.left = TreeNode(30)
    tree.root.left.right = TreeNode(40)
    tree.root.right.left = TreeNode(60)
    # print(tree.breadth_first())
    # tree.pre_order()
    # print("+++++++++++++++++")
    # tree.pre_order_iter()
# def pre_order_iter(self):
#     if not self.root:
#         return self.root
#
#     stack = Stack()
#     stack.push(self.root)
#
#     while not stack.is_empty():
#         top = stack.pop()
#         print(top.value)
#
#         if top.right:
#             stack.push(top.right)
#
#         if top.left:
#             stack.push(top.left)
