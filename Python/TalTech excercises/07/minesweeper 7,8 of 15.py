"""Minesweeper has to swipe the mines."""
import copy

def get_xzyq(minefield, i, j, height, width):
    """Return dimensions for units around a point."""
    x = i - 1
    if i == 0:
        x = 0
    z = j - 1
    if j == 0:
        z = 0
    y = i + 2
    if i + 2 > height:
        y = height
    q = j + 2
    if j + 2 > width:
        q = width
    return x, z, y, q


def create_minefield(height: int, width: int) -> list:
    """
    Create and return minefield.

    Minefield must be height high and width wide. Each position must contain single dot (`.`).
    :param height: int
    :param width: int
    :return: list
    """
    field = [["." for j in range(width)] for i in range(height)]
    return field


def add_mines(minefield: list, mines: list) -> list:
    """
    Add mines to a minefield and return minefield.

    This function cannot modify the original minefield list.
    Minefield must be length long and width wide. Each non-mine position must contain single dot.
    If a position is empty ("."), then a small mine is added ("x").
    If a position contains small mine ("x"), a large mine is added ("X").
    Mines are in a list.
    Mine is a list. Each mine has 4 integer parameters in the format [N, S, E, W].
        - N is the distance between area of mines and top of the minefield.
        - S ... area of mines and bottom of the minefield.
        - E ... area of mines and right of the minefield.
        - W ... area of mines and left of the minefield.
    :param minefield: list
    :param mines: list
    :return: list
    """
    result = copy.deepcopy(minefield)
    for x in range(len(mines)):
        low_h = mines[x][0]
        high_h = mines[x][1]
        high_h = len(result) - high_h
        right_w = mines[x][2]
        right_w = len(result[0]) - right_w
        left_w = mines[x][3]
        for height in range(low_h, high_h):
            for width in range(left_w, right_w):
                if result[height][width] == "x":
                    result[height][width] = "X"
                elif result[height][width] != "X":
                    result[height][width] = "x"
    return result


def get_minefield_string(minefield: list) -> str:
    """
    Return minefield's string representation.

    .....
    .....
    x....
    Xx...

    :param minefield:
    :return:
    """
    result = "".join("".join(minefield[0]))
    result = "".join("".join(minefield[i]) + "\n" for i in range(len(minefield)))
    result = result[:-1]
    return result


def calculate_mine_count(minefield: list) -> list:
    """
    For each cell in minefield, calculate how many mines are nearby.

    This function cannot modify the original list.
    So, the result should be a new list (or copy of original).

    ....
    ..x.
    X.X.
    x..X

    =>

    0111
    13x2
    X4X3
    x32X

    :param minefield:
    :return:
    """
    result = copy.deepcopy(minefield)
    height = len(minefield)
    width = len(minefield[0])
    for i in range(0, height):
        for j in range(0, width):
            if result[i][j] == "." or result[i][j] == "#":
                result[i][j] = 0
    for i in range(0, height):
        for j in range(0, width):
            x, z, y, q = get_xzyq(result, i, j, height, width)
            for ii in range(x, y):
                for jj in range(z, q):
                    if result[ii][jj] == "x" or result[ii][jj] == "X":
                        if result[i][j] != "x" and result[i][j] != "X":
                            result[i][j] += 1
            result[i][j] = str(result[i][j])
    return result


def walk(minefield, moves, lives) -> list:
    """Walk goes here."""
    return "a"