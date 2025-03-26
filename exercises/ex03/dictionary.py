"""Practice with Dictionary Functions"""

___author___: "730551362"


def invert(switch: dict[str, str]) -> dict[str, str]:
    inverted_value = {}
    for key in switch:
        value = switch[key]
        if value in inverted_value:
            raise KeyError("Cannot have multiple keys of the same value!")
        inverted_value[value] = key
    return inverted_value


def count(counting_list: list[str]) -> dict[str, int]:
    final_dictionary: dict[str, int] = {}
    for value in counting_list:
        if value in final_dictionary:
            final_dictionary[value] += 1
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
    color_dictionary = count(color_list)
    for color in color_dictionary:
        if color_dictionary[color] > max_number:
            max_number = color_dictionary[color]
            max_color = color
    return max_color


def bin_len(bin_list: list[str]) -> dict[int, set[str]]:
    index = 0
    bin_dictionary: dict[int, set[str]] = {}
    while index < len(bin_list):
        length = len(bin_list[index])
        if len(bin_list[index]) not in bin_dictionary:
            bin_dictionary[length] = {bin_list[index]}
        else:
            bin_dictionary[length].add(bin_list[index])
        index += 1

    return bin_dictionary
