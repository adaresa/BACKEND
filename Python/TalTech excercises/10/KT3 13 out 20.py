"""KT3 (R12)."""

def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if len(s) <= 1:
        return s
    lis = list(s)
    lis.insert(0, lis[-1])
    lis.pop(len(lis) - 1)
    return "".join(lis)


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    result = ""
    lis = list(text)
    index = 0
    for i in range(leave_count, len(text)):
        if index < take_count:
            result += lis[i]
            index += 1
        elif index < (take_count + leave_count):
            index += 1
        else:
            if take_count != 0:
                result += lis[i]
            index = 1
    return result


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], [], []]
    """
    return "temp"
    lis = []
    for _ in range(amount):
        lis.append(initial_list)
    if factor == 0:
        return lis
    print(lis[0][2])
    lis[0][2] = "?"
    print(lis[1][2])
    return lis