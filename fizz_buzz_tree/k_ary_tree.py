from stack_and_queue.stack_and_queue import *

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []


class KaryTrees:
    def __init__(self):
        self.root = None

    def level_order(self):
        if self.root is None:
            return 'You have an Empty Tree'
        q = Queue()
        q.enqueue(self.root)
        trees = []
        while not q.is_empty():
            node = q.dequeue()
            trees.append(node.value)
            for ch in node.children:
                q.enqueue(ch)
        return trees

    #
    # def breadth_order(self):
    #     q = Queue()
    #     q.enqueue(self.root)
    #
    #     if not self.root:
    #         return self.root
    #
    #     def _walk(node, breadth_list):
    #         pass
    #


if __name__ == '__main__':
    tree = KaryTrees()
    a = Node(5)
    tree.root = a
    b = Node(7)
    c = Node(15)
    s = Node(8)
    h = Node(95)
    a.children.append(b)
    a.children.append(c)
    a.children.append(s)
    b.children.append(h)

    # tree.root.children = Node(15)
    # tree.root.children = Node(19)
    # tree.root.children = Node(95)
    print(tree.level_order())

