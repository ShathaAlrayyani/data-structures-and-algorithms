from DS.linked_list.linked_list import LinkedList, Node

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

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()
        self._keys.append(key)
        self._buckets[hashed_key].add((key, value))

    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next

    def contains(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        if not bucket == None:
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False

    def keys(self):
        return self._keys
