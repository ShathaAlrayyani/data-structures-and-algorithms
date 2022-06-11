class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    # To create an empty Linked List
    def __init__(self):
        self.head = None

    # Adds a new node with that value to the head of the list with an O(1) Time performance.
    def insert(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Indicates whether that value exists as a Node’s value somewhere within the list.
    def include(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

    # Returns: a string representing all the values in the Linked List, formatted as:
    # "{ a } -> { b } -> { c } -> None"
    def to_string(self):
        linked_list = ''
        start = '{'
        end = '}'
        current = self.head
        while current:
            # we need to make sure the value added is a string, so we don't get any errors
            linked_list += f'{start} {current.value} {end} -> '
            current = current.next
        linked_list += " None"
        return linked_list


if __name__ == '__main__':
    node = LinkedList()
    node.insert(7)
    node.insert(12)
    node.insert(0)
    node.insert(13)
    node.insert(15)
    print(node.to_string())
