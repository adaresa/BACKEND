"""Program that creates beautiful pyramids."""

def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    height = int((base + 1) / 2)
    middle = int(base / 2)
    temp = 1
    if(base % 2 == 0):
        temp = 2
    pyramid = [[char if (middle - i - (1 * temp)) < j < (middle + i + 1) else " " for j in range(base)] for i in range(height)]
    return(pyramid)


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    temp = 0
    if len(pyramid_b) > len(pyramid_a):
        times = len(pyramid_b) - len(pyramid_a)
        while temp < times:
            pyramid_a.insert(0, [" "] * len(pyramid_a[0]))
            temp += 1
    else:
        times = len(pyramid_a) - len(pyramid_b)
        temp = 0
        while (temp < times):
            pyramid_b.insert(0, [" "] * len(pyramid_b[0]))
            temp += 1

    combined = [a + b for a, b in zip(pyramid_a, pyramid_b)]
    return combined


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    result = "".join("".join(pyramid[0]))
    result = "".join("".join(pyramid[i]) + "\n" for i in range(len(pyramid)))
    result = result[:-1]
    return result