from stack_and_queue.stack_and_queue import *

class EmptyQueueException(Exception):
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

        pre_order_list = []
        _walk(self.root, pre_order_list)
        return pre_order_list

    def in_order(self):
        """
        get the nodes from tree in depth-first left-root-right
        """
        if not self.root:
            return self.root

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

        in_order_list = []
        _walk(self.root, in_order_list)
        return in_order_list

    def post_order(self):
        """
        get the nodes from tree in depth-first left-right-root
        """
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

        post_order_list = []
        _walk(self.root, post_order_list)
        return post_order_list

    def find_max(self):
        if self.root is None:
            return None

        def _walk(root, max=0):
            if root is None:
                return max
            if max < root.value:
                max = root.value
            left_tree = _walk(root.left, max)
            if max < left_tree:
                max = left_tree
            right_tree = _walk(root.right, max)
            if max < right_tree:
                max = right_tree
            return max
        return _walk(self.root)

    def __str__(self):
        if self.root is None:
            return 'None'
        else:
            res_list = self.pre_order()
            output = ''
            for i in res_list:
                output += f'{i}'
            return output


if __name__ == '__main__':
    tree = BinaryTree()
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    print(tree.find_max())

