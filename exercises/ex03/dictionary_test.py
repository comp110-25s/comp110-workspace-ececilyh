"""Testing  Dictionary Functions"""

___author___: "730551362"

import pytest

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# Testing Invert
def test_invert() -> None:
    dictionary_test = {"1": "Emma", "2": "Cecily"}  # Creating dictionary test
    invert(dictionary_test) == {
        "Emma": "1",
        "Cecily": "2",
    }  # Passing it into invert (Checking that they equal each other!)


def test_invert2() -> None:
    dictionary_test2 = {}  # Creating dictionary test
    invert(dictionary_test2) == {}


def test_invert3() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


# Testing Favorite_Color
def test_favorite_color2() -> None:
    favcolor_test2 = {
        "Emma": "Blue",
        "Abby": "Pink",
        "Sophia": "Blue",
    }  # Creating dictionary test
    favorite_color(favcolor_test2) == "Blue"


def test_favorite_color() -> None:
    favcolor_test = {}  # Creating dictionary test
    favorite_color(favcolor_test) == ""


def test_favorite_color3() -> None:
    favcolor_test3 = {
        "E": "Blue",
        "A": "Pink",
        "S": "Blue",
        "B": "Pink",
    }  # Creating dictionary test
    favorite_color(favcolor_test3) == "Blue"


# Testing Count
def test_count() -> None:
    list_test1 = ["Blue", "Pink", "Purple", "Pink"]
    count(list_test1) == {"Blue": 1, "Pink": 2, "Purple": 1}


def test_count2() -> None:
    list_test2 = []
    count(list_test2) == {}


def test_count3() -> None:
    list_test3 = ["Blue", "Blue", "Purple", "Blue"]
    count(list_test3) == {"Blue": 3, "Purple": 1}


# Testing Bin_len
def test_bin_len() -> None:
    bin_dictionary_test = ["the", "quick", "fox"]
    bin_len(bin_dictionary_test) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    bin_dictionary_test2 = ["hello", "my", "name", "is"]
    bin_len(bin_dictionary_test2) == {2: {"my", "is"}, 4: {"name"}, 5: {"hello"}}


def test_bin_len3() -> None:
    bin_dictionary_test3 = []
    bin_len(bin_dictionary_test3) == {}
