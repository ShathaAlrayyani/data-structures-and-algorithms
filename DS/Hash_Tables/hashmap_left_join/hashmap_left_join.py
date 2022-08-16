from DS.Hash_Tables.hash_tables import *

def left_join(table1, table2):
    left_join_table = []
    for idx in table1.key():
        if table2.contains(idx):
            left_join_table.append([idx, table1.get(idx), table2.get(idx)])
        else:
            left_join_table.append([idx, table1.get(idx), 'Null'])
    return left_join_table
