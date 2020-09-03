"""Recursion is recursion."""

def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    recursive_reverse("") => ""
    recursive_reverse("abc") => "cba"

    :param s: string
    :return: reverse of s
    """
    # return s[::-1]
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def remove_nums_and_reverse(string):
    """
    Recursively remove all the numbers in the string and return reversed version of that string without numbers.

    print(remove_nums_and_reverse("poo"))  # "oop"
    print(remove_nums_and_reverse("3129047284"))  # empty string
    print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5oh565ty7p4"))  # "python for life"
    print(remove_nums_and_reverse("  k 4"))  # " k  "

    :param string: given string to change
    :return: reverse version of the original string, only missing numbers
    """
    # return("".join([i for i in string if not i.isdigit()][::-1]))
    char = ""
    if len(string) == 0:
        return string
    else:
        if not string[0].isdigit():
            char = string[0]
        return remove_nums_and_reverse(string[1:]) + char


def task1(string):
    """
    Figure out what this code is supposed to do and rewrite it using recursion.

    :param string: given string
    :return: figure it out
    """
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    if (len(string) - 1 > 0):
        return task1(string[1:-1])


def task2(string):
    """
    Figure out what this code is supposed to do and rewrite it using iteration.

    :param string: given string
    :return: figure it out
    """
    result = ""
    if len(string) < 2:
        return string
    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            result += string[i] + "-"
        else:
            result += string[i]
    result += string[-1]
    return result