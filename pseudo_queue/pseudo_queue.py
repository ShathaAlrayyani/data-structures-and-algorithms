from stack_and_queue.stack_and_queue import Stack


class IsEmpty(Exception):
    pass


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                data_moved = self.stack1.pop()
                self.stack2.push(data_moved)
        return self.stack2.pop()

    def __str__(self):
        current = self.stack1.top
        items = ''
        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items


if __name__ == '__main__':
    stack = PseudoQueue()
    stack.enqueue(1)
    stack.enqueue(3)
    stack.enqueue(5)
    stack.enqueue(7)
    print(stack.__str__())
    # print(stack.dequeue())
    print('after dequeue method')
    print(stack.dequeue())
    print(stack.__str__())
