import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

"""Testing  Dictionary Functions"""

___author___ = "730551362"


# Testing Invert
def test_invert() -> None:
    switch = {"1": "Emma", "2": "Cecily"}
    assert invert(switch) == {
        "Emma": "1",
        "Cecily": "2",
    }  # Use case that tests if the function inverts correctly.


def test_invert2() -> None:
    switch = {}  # Edge
    assert (
        invert(switch) == {}
    )  # Edge case that tests if the function correctly responds to an empty input.


def test_invert3() -> None:
    with pytest.raises(KeyError):
        switch = {"kris": "jordan", "michael": "jordan"}
        assert invert(
            switch
        )  # Use case that tests if the function correctly responds to incorrect inputs.


# Testing Favorite_Color
def test_favorite_color2() -> None:
    favcolor_test2 = {
        "Emma": "Blue",
        "Abby": "Pink",
        "Sophia": "Blue",
    }
    assert (
        favorite_color(favcolor_test2) == "Blue"
    )  # Use case that tests if the function correctly responds to a color represented multiple times.


def test_favorite_color() -> None:
    favcolor_test = {}
    assert (
        favorite_color(favcolor_test) == ""
    )  # Edge case that tests if the function correctly responds to an empty input.


def test_favorite_color3() -> None:
    favcolor_test3 = {
        "E": "Blue",
        "A": "Pink",
        "S": "Blue",
        "B": "Pink",
    }
    assert (
        favorite_color(favcolor_test3) == "Blue"
    )  # Use case that tests if the function correctly responds to multiple colors each represented multiple times.


# Testing Count
def test_count() -> None:
    list_test1 = ["Blue", "Pink", "Purple", "Pink"]
    assert count(list_test1) == {
        "Blue": 1,
        "Pink": 2,
        "Purple": 1,
    }  # Use case that tests if the function correctly responds to multiple colors.


def test_count2() -> None:
    list_test2 = []
    assert (
        count(list_test2) == {}
    )  # Edge case that tests if the function correctly responds to an empty input.


def test_count3() -> None:
    list_test3 = ["Blue", "Orange", "Pink", "Purple"]
    assert count(list_test3) == {
        "Blue": 1,
        "Orange": 1,
        "Pink": 1,
        "Purple": 1,
    }  # Use case that tests if the function correctly responds to four single colors.


# Testing Bin_len
def test_bin_len() -> None:
    bin_dictionary_test = ["the", "quick"]
    assert bin_len(bin_dictionary_test) == {
        3: {"the"},
        5: {"quick"},
    }  # Use case that tests that the function counts different lengths correctly.


def test_bin_len2() -> None:
    bin_dictionary_test2 = ["Hey", "I'm", "Ted"]
    assert bin_len(bin_dictionary_test2) == {
        3: {"Hey", "I'm", "Ted"},
    }  # Use case that tests that the function counts equal lengths correctly.


def test_bin_len3() -> None:
    bin_dictionary_test3 = []
    assert (
        bin_len(bin_dictionary_test3) == {}
    )  # Edge case that tests that the function correctly responds to an empty input.
