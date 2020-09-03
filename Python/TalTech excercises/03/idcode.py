# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""

def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if (gender_number > 0 and gender_number < 7):
        return True
    return False


def get_gender(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if (gender_number > 0 and gender_number < 7):
        if (gender_number == 1 or gender_number == 3 or gender_number == 5):
            return "male"
        else:
            return "female"
    return 'error'


def is_leap_year(year_number: int) -> bool:
    """
    Check if given value is correct for leap year in ID code.

    :param year_number: int
    :return: boolean
    """
    return year_number % 4 == 0 and (year_number % 100 != 0 or year_number % 400 == 0)


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if (year_number >= 0 and year_number <= 99):
        return True
    return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if (month_number >= 1 and month_number <= 12):
        return True
    return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    year = get_full_year(gender_number, year_number)
    if month_number in {1, 3, 5, 7, 8, 10, 12}:
        num_days = 31
    if month_number == 2:
        if is_leap_year(year) is True:
            num_days = 29
        else:
            num_days = 28
    else:
        num_days = 30
    if (day_number <= num_days and day_number > 0):
        return True
    return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if (birth_number > 0 and birth_number < 1000):
        return True
    return False


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    check_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    check_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    kood = [int(x) for x in id_code]
    calc_1 = sum(x * y for x, y in zip(kood, check_1)) % 11
    calc_2 = sum(x * y for x, y in zip(kood, check_2)) % 11

    if calc_1 != 10:
        number = calc_1
    elif calc_2 != 10:
        number = calc_2
    else:
        number = 0

    if int(id_code[10]) == number:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    year = ''
    digits = year_number

    if gender_number == 1 or gender_number == 2:
        year += '18'
    if gender_number == 3 or gender_number == 4:
        year += '19'
    if gender_number == 5 or gender_number == 6:
        year += '20'
    if year_number < 10:
        year += '0'
    year += str(digits)
    return int(year)


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    city = {
        11: "Kuressaare",
        21: "Tartu",
        221: "Tallinn",
        271: "Kohtla-Järve",
        371: "Tartu",
        421: "Narva",
        471: "Pärnu",
        491: "Tallinn",
        521: "Paide",
        571: "Rakvere",
        601: "Valga",
        651: "Viljandi",
        711: "Võru",
        1000: "undefined"
    }
    if birth_number > 0 and birth_number < 1000:
        for x in city.keys():
            if (birth_number < x):
                return city[x]
    else:
        return "Wrong input!"


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if is_id_valid(id_code) is False:
        return "Given invalid ID code!"
    gender = get_gender(int(id_code[0]))
    birthday = id_code[5] + id_code[6] + "." + id_code[3] + id_code[4] + "." + str(get_full_year(int(id_code[0]), int(id_code[1] + id_code[2])))
    place = get_birth_place(int(id_code[7] + id_code[8] + id_code[9]))
    return f"This is a {gender} born on {birthday} in {place}."


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    if id_code.upper().isupper() is False:
        if len(id_code) == 11:
            if is_valid_gender_number(int(id_code[0])):
                if is_valid_year_number(int(id_code[1] + id_code[2])):
                    if is_valid_month_number(int(id_code[3] + id_code[4])):
                        if is_valid_day_number(int(id_code[0]), int(id_code[1] + id_code[2]), int(id_code[3] + id_code[4]), int(id_code[5] + id_code[6])):
                            if is_valid_birth_number(int(id_code[7] + id_code[8] + id_code[9])):
                                if is_valid_control_number(id_code):
                                    return True
    return False