class IsEmpty(Exception):
    pass


class AnimalShelter(object):
    def __init__(self):
        self.dogs = None
        self.cats = None
        self.order = 0

    """
    @param {string} name
    @param {string} type Animal is dog or cat
    @return nothing
    """

    def enqueue(self, name, type):
        if type == 'dog':
            self.dogs = name
            self.order += 1
        elif type == 'cat':
            self.cats = name
            self.order += 1

    # return a string
    def dequeue(self):
        cats = []
        dogs = []
        if not self.dogs and not self.cats:
            raise IsEmpty('the list is empty')
        if self.cats:
            removed = self.cats[0]
            self.cats = self.cats[1]
            removed.next = None
            return removed.value
        if self.dogs:
            removed = self.dogs
            self.dogs = self.dogs
            removed.next = None
            return removed.value

    # def __str__(self):
    #     current = self.cats
    #     current2 = self.dogs
    #     item1 = ''
    #     item2 = ''
    #     if current is None and current2 is None:
    #         raise IsEmpty('lists are empty')
    #     while current:
    #         item1 += f"{current} \n"
    #         current = current.next
    #     while current2:
    #         item2 += f"{current2} \n"
    #         current2 = current2.next
    #
    #     return item1, item2


if __name__ == '__main__':
    stack = AnimalShelter()
    stack.enqueue('candy', 'cat')
    stack.enqueue('rocky', 'dog')
    # stack.enqueue(5)
    # stack.enqueue(7)
    # print(stack.__str__())
    # print(stack.dequeue())
    print('after dequeue method')
    stack.dequeue()

