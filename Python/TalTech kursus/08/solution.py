"""EX08 Solution and Test."""

def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if (18 <= time <= 24):
        return True
    if (5 <= time <= 17):
        if coffee_needed is True:
            return True
        return False
    return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    if a == b and b == c:
        return 5
    if a != b and a != c:
        return 1
    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    result = 0
    while big_baskets > 0 and ordered_amount > 4:
        big_baskets -= 1
        ordered_amount -= 5
    while small_baskets > 0 and ordered_amount > 0:
        small_baskets -= 1
        ordered_amount -= 1
        result += 1
    if ordered_amount == 0:
        return result
    return -1