class Node:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n


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
        linked_list += "None"
        return linked_list

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


    def insert_before(self, val1, val2):
        """ALGORITHM AddBefore(newValue, valueToAddBefore)
// INPUT <-- New value, Value to add before
// OUTPUT <-- boolean

  Current <-- Head

  IF Current is equal to NULL
    return FALSE

  WHILE Current.Next is not equal to NULL
    IF Current.Next.Value is equal to valueToAddBefore
      newNode <-- NEW Node
      newNode.Value <-- newValue
      newNode.Next <-- Current.Next
      Current.Next <-- newNode
      return TRUE

    Current <-- Current.Next;

  return FALSE"""
        new_node = Node(val1)
        current = self.head

        if current is None:
            return False

        else:
            while current.next is not None:
                if current.next.value == val2:
                    new_node.value = val1
                    new_node.next = current.next
                    current.next = new_node
                    return True
                current = current.next

    def insert_after(self, val1, val2):
        new_node = Node(val2)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if current == Node(val1):
                    current.next = new_node
                current = current.next




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
    node.append(14)
    node.append(17)
    node.append(20)
    print(node.to_string())
    node.insert_before(0, 9)
    print(node.to_string())
    # node.insert_after(0, 24)
    # print(node.to_string())

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
