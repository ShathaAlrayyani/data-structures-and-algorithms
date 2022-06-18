class Node:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n


class LinkedList:
    # To create an empty Linked List
    def __init__(self):
        self.head = None

    def insert(self, val):
        """Adds a new node with that value to the head of the list with an O(1) Time performance.
        input :"""
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Indicates whether that value exists as a Node’s value somewhere within the list.
    def include(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

    def to_string(self):
        """Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> None" """
        linked_list = ''
        start = '{'
        end = '}'
        current = self.head
        while current:
            # we need to make sure the value added is a string, so we don't get any errors
            linked_list += f'{start} {current.value} {end} -> '
            current = current.next
        linked_list += "None"
        return linked_list

    def append(self, val):
        new_node = Node(val)
        current = self.head

        if self.head is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_before(self, val1, val2):
        """It is method to insert new node before a specific """
        new_node = Node(val2)
        current = self.head
        if current is None:
            return "you have an empty linked-list"
        elif current.value == val1:
            return self.insert(val2)
        else:
            while current.next is not None:
                if current.next.value == val1:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            return True


    def insert_after(self, val1, val2):
        new_node = Node(val2)
        current = self.head

        if current is None:
            return "you have an empty linked-list"
        else:
            while current is not None:
                if current.value == val1:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            return True


    def linked_list_kth(self, k):
        current = self.head
        node_list = []
        while current is not None:
            node_list.append(current)
            current = current.next
        list_len = len(node_list)
        if len(node_list) > 1:
            if k < 0:
                return 'This value is not accepted'
            elif k < list_len:
                return node_list[list_len - (k+1)].value
            else:
                return 'This value is not found'
        else:
            return 'the list is empty'


if __name__ == '__main__':
    node = LinkedList()
    node.insert(7)
    node.insert(12)
    node.insert(0)
    node.insert(13)
    node.insert(15)
    print(node.to_string())
    node.append(5)
    node.append(6)
    print(node.to_string())
    node.insert_before(15, 17)
    node.insert_after(5, 2)
    node.append(20)
    print(node.to_string())
    code2 = node.linked_list_kth(0)
    print(code2)

#
# class Node:
#     def __int__(self, val):
#         self.value = val
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def __add__(self, val):
#
