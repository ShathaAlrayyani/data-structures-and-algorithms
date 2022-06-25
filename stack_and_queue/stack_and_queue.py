class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
      A stack is a data structure that consists of Nodes. Each Node
      references the next Node in the stack, but does not reference its
      previous.
      """

    def __init__(self):
        self.top = None

    def push(self, value):
        """To add new node to the top """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """To remove the top value"""
        if self.top is None:
            raise Exception("the list is empty")
        else:
            removed = self.top
            self.top = self.top.next
            removed.next = None
            return removed.value

    def peek(self):
        if self.top is None:
            raise Exception("the list is empty")
        else:
            value = self.top.value
            return value

    def is_empty(self):
        return True if self.top is None else False

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise Exception("the list is empty")
        else:
            removed = self.front
            self.front = self.front.next
            removed.next = None
            return removed.value

    def peek(self):
        if self.front is None:
            raise Exception("the list is empty")
        else:
            return self.front.value

    def is_empty(self):
        return True if self.front is None else False

    def __str__(self):
        current = self.front
        items = ''
        while current:
            items += f"{current.value} \n"
            current = current.next

        return items


if __name__ == '__main__':
    node = Stack()
    node.push(0)
    node.push(2)
    node.push(4)
    node.push(6)
    node.push(8)
    print(node.__str__())
    node2 = Queue()
    node2.enqueue(1)
    node2.enqueue(3)
    node2.enqueue(5)
    node2.enqueue(7)
    node2.enqueue(9)
    print(node2.__str__())
