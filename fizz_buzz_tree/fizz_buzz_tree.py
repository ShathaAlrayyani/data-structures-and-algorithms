from stack_and_queue.stack_and_queue import *


def fizz_buzz_tree(tree):
    """
    Determine whether the value of each node is divisible by 3, 5 or both.
    Create a new tree with the same structure as the original, but the values modified
    """
    if not tree.root:
        return "The Tree is empty"
    new_tree = ''
    # new_tree = []
    val = tree.root
    while val in tree:
        new_tree = ''
        if val % 3 == 0:
            new_tree += 'Fizz'

        elif val % 5 == 0:
            new_tree += 'Buzz'
        elif val % 3 == 0 and val % 5 == 0:
            new_tree += 'FizzBuzz'
        else:
            new_tree += str(val)

    # def _walk(val):
    #
    #     new_tree = ''
    #     if val % 3 == 0:
    #         new_tree += 'Fizz'
    #
    #     elif val % 5 == 0:
    #         new_tree += 'Buzz'
    #     elif val % 3 == 0 and val % 5 == 0:
    #         new_tree += 'FizzBuzz'
    #     else:
    #         new_tree += str(val)


    qu = Queue()
    qu.enqueue(tree.root)
