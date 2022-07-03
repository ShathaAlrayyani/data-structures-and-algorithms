import pytest
from animal_shelter.animal_shelter import *


def test_enqueue_single_cat():
    """
    tset enqueue single cat and check the dequeue based on pref
    """
    shelter = AnimalShelter()
    cat = Cat('sherry')
    shelter.enqueue(cat)
    actual = shelter.dequeue('cat')
    expected = cat
    assert actual == expected


def test_enqueue_single_dog():
    """
    tset enqueue single dog and check the dequeue based on pref
    """
    shelter = AnimalShelter()
    dog = Dog('Alex')
    shelter.enqueue(dog)
    actual = shelter.dequeue('dog')
    expected = dog
    assert actual == expected


def test_dequeue_Pref_dog_but_front_is_cat():
    """
    tset dequeue if the pref is dog and the front is cat
    """
    shelter = AnimalShelter()
    cat = Cat('sherry')
    dog = Dog('Alex')
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue('dog')
    expected = dog
    assert actual == expected


def test_dequeue_pref_cat_but_front_is_dog():
    """
    tset dequeue if the pref is cat and the front is dog
    """
    shelter = AnimalShelter()
    dog = Dog('Alex')
    cat = Cat('sherry')
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    actual = shelter.dequeue('cat')
    expected = cat
    assert actual == expected


def test_dequeue_preff_cat_but_front_is_dog():
    """
    tset multi enqueue and dequeue if the pref is cat and the front is dog
    """
    shelter = AnimalShelter()
    dog1 = Dog('Alex')
    cat1 = Cat('sherry')
    dog2 = Dog('Alex')
    cat2 = Cat('sherry')
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(dog2)
    shelter.enqueue(cat2)
    actual = shelter.dequeue('cat')
    expected = cat1
    assert actual == expected


def test_dequeue_invalid_pref():
    """
    test dequeue if the pref is invalid ( not a cat or not a dog )
    """
    shelter = AnimalShelter()
    dog = Dog('Alex')
    cat = Cat('sherry')
    dog2 = Dog('Alex')
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.enqueue(dog2)
    actual = shelter.dequeue('crocodile')
    expected = None
    assert actual == expected

