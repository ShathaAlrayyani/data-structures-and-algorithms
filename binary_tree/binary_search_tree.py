try:
    from binary_tree import *
except:
    from binary_tree.binary_tree import *


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        """"""
        if self.root is None:
            self.root = Node(value)

        def _walk(rt, val):

            if rt is None:
                rt = Node(val)
                return rt
            elif val > rt.value:
                if rt.right is None:
                    rt.right = Node(val)
                else:
                    _walk(rt.right, val)
            elif val < rt.value:
                if rt.left is None:
                    rt.left = Node(val)
                else:
                    _walk(rt.left, val)
            else:
                _walk(rt.right, val)

        return _walk(self.root, value)

    def contains(self, value):

        if self.root is None:
            return False
        rt = self.root
        while rt:
            if rt.value == value:
                return True
            elif value > rt.value:
                rt = rt.right
            else:
                rt = rt.left
        return False


if __name__ == '__main__':
    btree = BinarySearchTree()
    btree.add(10)
    btree.add(15)
    btree.add(7)
    btree.add(19)
    btree.add(9)
    btree.add(5)
    btree.add(25)
    print(btree.pre_order())
    print(btree.contains(25))
