import pytest
from animal_shelter.animal_shelter import *


def test_enqueue_single_cat():
    """
    tset enqueue single cat and check the dequeue based on pref
    """
    shelter = AnimalShelter()
    cat = 'sherry'
    shelter.enqueue(cat)
    actual = shelter.dequeue('cat')
    expected = cat
    assert actual == expected


def test_enqueue_single_dog():
    """
    tset enqueue single dog and check the dequeue based on pref
    """
    shelter = AnimalShelter()
    dog = 'Alex'
    shelter.enqueue(dog)
    actual = shelter.dequeue('dog')
    expected = dog
    assert actual == expected



