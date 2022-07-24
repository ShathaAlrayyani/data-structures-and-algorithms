from stack_and_queue.stack_and_queue import *

class EmptyTree(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    """
    Define a method for each type of the Depth-first-Tree
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        get the nodes from tree in depth-first root-left-right
        """
        if not self.root:
            return self.root
        pre_order_list = []

        def _walk(node, curr_list):
            """
            store the value of nodes recursively
            """
            if node:
                curr_list.append(node.value)
                if node.left is not None:
                    _walk(node.left, curr_list)
                if node.right is not None:
                    _walk(node.right, curr_list)
            return curr_list


        _walk(self.root, pre_order_list)
        return pre_order_list

    def in_order(self):
        """
        get the nodes from tree in depth-first left-root-right
        """
        if not self.root:
            return self.root
        in_order_list = []

        def _walk(node, curr_list):
            """
            store the value of nodes recursively
            """
            if node.left is not None:
                _walk(node.left, curr_list)
            curr_list.append(node.value)
            if node.right is not None:
                _walk(node.right, curr_list)
            return curr_list

        _walk(self.root, in_order_list)
        return in_order_list

    def post_order(self):
        """
        get the nodes from tree in depth-first left-right-root
        """
        post_order_list = []

        def _walk(node, curr_list):
            """
            store the value of nodes recursively
            """
            if node.left is not None:
                _walk(node.left, curr_list)
            if node.right is not None:
                _walk(node.right, curr_list)
            curr_list.append(node.value)
            return curr_list

        _walk(self.root, post_order_list)
        return post_order_list

    def find_max(self):
        if self.root is None:
            return None

        def _walk(root, m=0):
            if root is None:
                return m
            if m < root.value:
                m = root.value
                _walk(root.left, m)
            if m < root.left.value:
                m = root.left
                _walk(root.right, m)
            if m < root.right.value:
                m = root.right
            return m

        return _walk(self.root)

    def __str__(self):
        if self.root is None:
            return 'None'
        else:
            n_list = self.pre_order()
            output = ''
            for n in n_list:
                output += f'{n}'
            return output


# class BinarySearchTree(BinaryTree):
#     def __init__(self):
#         super().__init__()
#
#     def add(self, value):
#         """"""
#         if self.root is None:
#             self.root = Node(value)
#
#         def _walk(root, val):
#
#             if root is None:
#                 root = Node(val)
#                 return root
#             elif root.value <= val:
#                 _walk(root.right, val)
#             else:
#                 _walk(root.left, val)
#
#         return _walk(self.root, value)
#
#     def contains(self, value):
#         if self.root is None:
#             return False
#
#         def _walk(root, val):
#             if root.value is val:
#                 return True
#             elif val < root.value:
#                 _walk(root.left, val)
#             elif val > root.value:
#                 _walk(root.right, val)
#             else:
#                 return False
#         return _walk(self.root, value)



if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(15)
    tree.root.left = Node(7)
    tree.root.right = Node(19)
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    print(tree.find_max())



