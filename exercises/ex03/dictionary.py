"""Practice with Dictionary Functions"""

___author___: "730551362"


def invert(dict: dict[str, str]) -> dict[str, str]:
    inverted_value = {}
    for key in dict:
        value = dict[key]
        if value in inverted_value:  # Need to check for error before we add keys.
            raise KeyError("Cannot have multiple keys of the same value!")
        inverted_value[value] = key
    return inverted_value


def count(list: list[str]) -> dict[str, int]:
    final_dictionary: dict[str, int] = {}
    idx = 0
    for value in final_dictionary:
        if value in final_dictionary:
            final_dictionary[value] += 1
            idx += 1
        else:
            final_dictionary[value] = 1
    return final_dictionary


def favorite_color(names_colors: dict[str, str]) -> str:
    color_dictionary: dict[str, int] = {}
    color_list = []
    max_number = 0
    max_color = ""
    for name in names_colors:
        color_list.append(names_colors[name])
    color_dictionary = count(color_list)  # Now stored in count_dictionary
    for color in color_dictionary:  # Never need to do an index.
        if (
            color_dictionary[color] > max_number
        ):  # Only update if it is MORE, that way we don't update if they are the same.
            max_number = color_dictionary[color]
            max_color = color
    return max_color


def bin_len(bin_list: list[str]) -> dict[int, dict]:
    index = 0
    bin_dictionary: dict[int, dict] = {}
    while index < len(bin_list):
        length = len(bin_list[index])
        if len(bin_list[index]) not in bin_dictionary:
            bin_dictionary[length] = {bin_list[index]}
        else:
            bin_dictionary[length].add(bin_list[index])
        index += 1

    return bin_dictionary
