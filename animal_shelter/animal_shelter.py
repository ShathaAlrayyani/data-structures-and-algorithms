from stack_and_queue.stack_and_queue import Queue

class AnimalShelter:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        """
        adds a new animal with that value to the back of the queue with an O(1) Time performance.
        """

        animal = Queue()
        if not self.rear:
            self.front = animal
            self.rear = animal
        else:
            self.rear.next = animal
            self.rear = animal


    def dequeue(self, pref):
        """
        Returns: the pref animal if it was the front but if the front not equal
        to pref it will remove it and then re add it to the queue
        then keeps doing it until it matches the preference
        """
        if self.rear is not None:
            if pref == 'dog' or pref == 'cat':

                while self.front.data != pref:
                    selected_animal = self.front
                    self.front = self.front.next
                    selected_animal.next = None
                return selected_animal.data
            else:
                return None
        else:
            raise Exception('queue is empty')
