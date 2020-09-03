"""Filtering."""

def remove_vowels(string: str) -> str:
    """
    Remove vowels (a, e, i, o, u).

    :param string: Input string
    :return string without vowels.
    """
    a = string
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in string:
        if x in vowels:
            a = a.replace(x, "")
    return a


def longest_filtered_word(string_list: list) -> str:
    """
    Filter, find and return the longest string.

    :param string_list: List of strings.
    :return: Longest string without vowels.
    """
    i = 0
    while i < len(string_list):
        string_list[i] = remove_vowels(string_list[i])
        i += 1
    string_list.sort(key=len, reverse=True)
    return string_list[0]


def sort_list(string_list: list) -> list:
    """
    Filter vowels in strings and sort the list by the length.

    Longer strings come first.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of symbols in descending order.
    """
    i = 0
    while i < len(string_list):
        string_list[i] = remove_vowels(string_list[i])
        i += 1
    string_list.sort(key=len, reverse=True)
    return string_list