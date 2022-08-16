
import pytest

from DS.Hash_Tables.hashmap_left_join.hashmap_left_join import *
from DS.Hash_Tables.hash_tables import Hashtable

def test_left_join(sample_left_table, sample_right_table):
    actual = left_join(sample_left_table, sample_right_table)
    expected = [
        ['font', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', 'idle'],
        ['outfit', 'garb', 'Null'],
        ['guide', 'usher', 'follow']
    ]
    assert actual == expected


@pytest.fixture
def sample_left_table():
    sample_left_table = Hashtable()
    arr1 = [
        ["font", "enamored"],
        ["wrath", "anger"],
        ["diligent", "employed"],
        ["outfit", "garb"],
        ["guide", "usher"]
    ]
    for i in range(len(arr1)):
        sample_left_table.set(arr1[i][0], arr1[i][1])

    return sample_left_table


@pytest.fixture
def sample_right_table():
    sample_right_table = Hashtable()
    arr2 = [
        ["font", "averse"],
        ["wrath", "delight"],
        ["diligent", "idle"],
        ["flow", "jam"],
        ["guide", "follow"]
    ]
    for i in range(len(arr2)):
        sample_right_table.set(arr2[i][0], arr2[i][1])

    return sample_right_table


