from DS.Trees.fizz_buzz_tree.k_ary_tree import *

def fizz_buzz_tree(tr):
    """
    Determine whether the value of each node is divisible by 3, 5 or both.
    Create a new tree with the same structure as the original, but the values modified
    """
    if not tr:
        return "The Tree is empty"
    new_tree = []
    i = 0
    while i in range(len(tr)):
        val = tr[i]
        if val % 3 == 0 and val % 5 == 0:
            new_tree.append('FizzBuzz')
            i += 1
        elif val % 5 == 0:
            new_tree.append('Buzz')
            i += 1
        elif val % 3 == 0:
            new_tree.append('Fizz')
            i += 1
        else:
            new_tree.append(str(val))
            i += 1
    return new_tree


if __name__ == '__main__':
    tree = KaryTrees()
    a = Node(5)
    tree.root = a
    b = Node(7)
    c = Node(15)
    s = Node(8)
    h = Node(95)
    a.children.append(b)
    a.children.append(c)
    a.children.append(s)
    b.children.append(h)

    print(fizz_buzz_tree(tree.level_order()))
