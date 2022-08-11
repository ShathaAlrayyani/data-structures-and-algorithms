from DS.Hash_Tables.hashmap_repeated_word import *
import pytest

def test_no_repeated_word():
    actual = repeat_word("This is just a test")
    expected = "No Repeated Word Found"
    assert actual == expected


def test_string_one():
    actual = repeat_word("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected


def test_string_two():
    actual = repeat_word(
        "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of ")
    expected = "it"
    assert actual == expected


def test_string_three():
    actual = repeat_word(
        "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was "
        "doing in New York...")
    expected = "summer"
    assert actual == expected