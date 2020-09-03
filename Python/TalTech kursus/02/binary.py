"""Converter."""

def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    if dec == 0 or dec == 1:
        return str(dec)
    value = ""
    while dec != 0:
        a = dec % 2
        dec = dec // 2
        value = str(a) + value
    return str(value)


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    int_binary = int(binary)
    value = 0
    power = 0
    while int_binary > 0:
        value += 2 ** power * (int_binary % 10)
        int_binary //= 10
        power += 1
    return value