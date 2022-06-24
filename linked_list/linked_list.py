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
        """It is method to insert new node before a specific node"""
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
        """It is method to insert new node after a specific node"""
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
        """It is method to get a specific node with index of k starting from the end of the linked list"""
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
                return node_list[list_len - (k + 1)].value
            else:
                return 'This value is not found'
        else:
            return 'the list is empty'

    @staticmethod
    def linked_list_zip(p, s):
        """Zip the two linked lists together into one so that the nodes
        alternate between the two lists and return a reference to the zipped list"""
        p_curr = p.head
        s_curr = s.head
        if p_curr is None or s_curr is None:
            return False
        # swap their positions until one finishes off
        while p_curr and s_curr:
            # To Save next pointers
            p_next = p_curr.next
            s_next = s_curr.next

            # to make q_curr next of p_curr
            s_curr.next = p_next  # change next pointer of s_curr
            p_curr.next = s_curr  # change next pointer of p_curr
            last_p_curr = p_curr.next  # return the pointer of the first list to its origin.

            # update current pointers for next iteration
            p_curr = p_next
            s_curr = s_next

            # this if statement means when the first list is shorter than the other list the function will continue
            # till the second linked list end
            if not p_curr and s_curr:
                last_p_curr.next = s_curr
        return True


    # @staticmethod
    # def palindrome(ll):
    #     current = ll.head
    #     node_list = []
    #     new_list = []
    #     while current is not None:
    #         node_list.append(current.value)
    #         current = current.next
    #     for i in range(len(node_list) - 1, -1, -1):
    #         new_list.append(node_list[i])
    #     if node_list == new_list:
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    node = LinkedList()
    node.insert(1)
    node.insert(3)
    node.insert(1)
    # node.append(7)
    # node.append(9)
    # node.insert_before(15, 17)
    # node.insert_after(5, 2)
    print(node.to_string())
    # code2 = node.linked_list_kth(0)
    # print(code2)
    node2 = LinkedList()
    node2.append(0)
    node2.append(2)
    node2.append(4)
    # node2.append(6)
    # # node2.append(8)
    # print(node2.to_string())
    # # node.linked_list_zip(node, node2)
    # print(node.to_string())


    # {t}->{a}->{c}->{o}->{c}->{a}->{t}
    node3 = LinkedList()
    node3.append("t")
    node3.append("a")
    node3.append("c")
    node3.append("o")
    node3.append("c")
    node3.append("a")
    node3.append("t")
    dana = node3.palindrome(node3)
    print(dana)

