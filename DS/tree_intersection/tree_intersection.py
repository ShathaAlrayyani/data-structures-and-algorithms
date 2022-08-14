from DS.Hash_Tables.hash_tables import *
from DS.Trees.binary_tree.binary_tree import *

def tree_intersection(bt1, bt2):
    b_tree1 = bt1.pre_order()
    b_tree2 = bt2.pre_order()

    h_table = Hashtable()
    new_tree = []
    for value in b_tree1:
        h_table.set(key=str(value), value=value)
    for value in b_tree2:
        if h_table.contains(str(value)):
            new_tree.append(value)
    return new_tree

