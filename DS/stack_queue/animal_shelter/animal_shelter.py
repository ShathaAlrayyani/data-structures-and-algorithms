from DS.stack_queue.stack_and_queue.stack_and_queue import Queue

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        """
        this method will enqueue Dogs to dogs Queue and Cats to cats Queue
        """
        if animal.type == 'Dog':
            self.dogs.enqueue(animal)
        elif animal.type == 'Cat':
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        """
        this method will take a pref as a parameter and
        if the pref is cat, dequeue from cats Queue
        if the pref is dogs, dequeue from dogs Queue
        """
        if pref == 'dog':
            return self.dogs.dequeue()
        elif pref == 'cat':
            return self.cats.dequeue()
        else:
            return None


class Dog:
    def __init__(self, name):
        self.type = 'Dog'
        self.name = name


class Cat:
    def __init__(self, name):
        self.type = 'Cat'
        self.name = name
