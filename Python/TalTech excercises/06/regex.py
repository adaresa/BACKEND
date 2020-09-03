"""Using regex."""
import re

def read_file(path: str) -> list:
    """
    Read file and return list of lines read.

    :param path: str
    :return: list
    """
    with open(path, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def match_specific_string(input_data: list, keyword: str) -> int:
    """
    Check if given list of strings contains keyword.

    Return all keyword occurrences (case insensitive). If an element cointains the keyword several times, count all the occurrences.

    ["Python", "python", "PYTHON", "java"], "python" -> 3

    :param input_data: list
    :param keyword: str
    :return: int
    """
    if keyword == "":
        return 0
    textLower = [item.lower() for item in input_data]
    keywordLower = keyword.lower()
    a = 0
    for element in textLower:
        for word in element.split():
            if re.findall(keywordLower, word):
                a += 1
    return a


def detect_email_addresses(input_data: list) -> list:
    """
    Check if given list of strings contains valid email addresses.

    Return all unique valid email addresses in alphabetical order presented in the list.
    ["Test", "Add me test@test.ee", "ago.luberg@taltech.ee", "What?", "aaaaaa@.com", ";_:Ö<//test@test.au??>>>;;d,"] ->
    ["ago.luberg@taltech.ee", "test@test.au", "test@test.ee"]

    :param input_data: list
    :return: list
    """
    newlist = []
    for element in input_data:
        newlist.append((re.findall(r"[a-zA-Z0-9][a-zA-Z0-9_+-.]{0,63}[a-zA-Z0-9]{1}@[a-zA-Z0-9_+-]{1,254}.[a-zA-Z.]{1,63}[a-zA-Z]{1}", element)))
    newlist = list(filter(None, newlist))
    newlist.sort()
    flatlist = [item for sublist in newlist for item in sublist]
    flatlist = list(dict.fromkeys(flatlist))
    return flatlist