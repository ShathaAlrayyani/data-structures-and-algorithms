class Node:
    """
    Node Instantiate.
    This class will have only an __init__ method to create nodes.
    """

    def __init__(self, value, next=None):
        """
        Takes two arguments:
        1. Value: str, int, ..., etc.
        2. Next: Node
        returns: None
        """
        self.value = value
        self.next = next


class LinkedList:
    """
    A Linked List class with a single head node
    """

    def __init__(self):
        """
        Instantiates a singly-linked list with an empty head node.
        Args: head (None by default)
        Outputs: None
        """
        self.head = None

    def insert(self, value):
        """
        This method will insert a node at the start of the linked list
        arguments : value
        returns:None
        """
        node = Node(value)
        node.next = self.head
        self.head = node


class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size
        self._keys = []

    def _hash(self, key):
        hash_total = sum([ord(i) for i in key])
        return (hash_total * 211) % self._size

    def set(self, key, value):
        hashed_key = self._hash(key)
        hash_list = LinkedList()
        self._buckets[hashed_key] = hash_list
        self._keys.append(key)
        hash_list.insert((key, value))

    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key] = LinkedList()

        current = bucket.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next

    def contains(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key] = LinkedList()

        if bucket is not None:
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False

    def keys(self):
        return self._keys

