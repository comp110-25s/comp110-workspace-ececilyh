"""Testing  Dictionary Functions"""

___author___: "730551362"

import pytest

from exercises.ex03.dictionary import invert


def test_invert() -> None:
    dictionary_test = {"1": "Emma", "2": "Cecily"}  # Creating dictionary test
    invert(dictionary_test) == {
        "Emma": "1",
        "Cecily": "2",
    }  # Passing it into invert (Checking that they equal each other!)


def test_invert2() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count


def test_favorite_color() -> None:
    favcolor_test = {}  # Creating dictionary test
    favorite_color(favcolor_test) == {}


from exercises.ex03.dictionary import bin_len


def test_bin_len() -> None:
    bin_dictionary_test = ["the", "quick", "fox"]
    bin_len(bin_dictionary_test) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    bin_dictionary_test2 = ["hello", "my", "name", "is"]
    bin_len(bin_dictionary_test2) == {2: {"my", "is"}, 4: {"name"}, 5: {"hello"}}
