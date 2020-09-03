"""Create schedule from the given file."""
import re
from datetime import datetime

def is_hour_legit(hour: str) -> bool:
    """Check if hour number is legit."""
    if int(hour) < 24:
        return True
    return False


def is_minute_legit(minute: str) -> bool:
    """Check if minute number is legit."""
    if int(minute) < 60:
        return True
    return False


def is_short_hour(a: dict):
    """Check if all hour numbers are one digit."""
    length = len(a)
    count = 0
    for keys in a:
        if keys[0] == " ":
            count += 1
        if count == length:
            return 1
    return 0


def create_schedule_dict(input_string: str) -> dict:
    """Make schedule into dictionary format."""
    dict1 = {}
    dict2 = {}
    reg = r"(?<!\S)([0-9]{1,2})\D([0-9]{1,2})\s+([a-zA-Z]{1,99})"
    for match in re.finditer(reg, input_string):
        cont = True
        hour = match.group(1)
        minute = match.group(2)
        if is_hour_legit(hour) is False:
            cont = False
        if is_minute_legit(minute) is False:
            cont = False
        if len(hour) == 1:
            hour = "0" + hour
        if len(minute) == 1:
            minute = "0" + minute
        time = hour + ":" + minute
        action = match.group(3)
        action = str.lower(action)
        if cont is True:
            if time in dict1:
                dict1[time].append(action)
            else:
                dict1[time] = [action]
    for key, value in dict1.items():
        unique = []
        [unique.append(item) for item in value if item not in unique]
        dict1[key] = unique

    for key in sorted(dict1.keys()):
        dict2[key] = dict1[key]
    return dict2


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    dict = create_schedule_dict(input_string)
    dict = normalize(dict)
    table = []

    longa, longb = get_table_sizes(dict)

    spacea = " " * (longa - len("time"))
    spaceb = " " * (longb - len("items"))

    table.append("-" * (longa + longb + 7))
    table.append("| " + spacea + "time | items" + spaceb + " |")
    table.append("-" * (longa + longb + 7))
    for key, value in dict.items():
        spacea = " " * (longa - len(key))
        spaceb = " " * (longb - len(", ".join(value)))
        x = False
        short1 = 1
        if is_short_hour(dict) == 1:
            short1 = 0
            table[0] = ("-" * (longa + longb + 6))
            table[1] = ("|    " + spacea + "time | items" + " |")
            table[2] = ("-" * (longa + longb + 6))
            x = True
        temp1 = " " * short1
        table.append("|" + temp1 + key + spacea + " | " + ", ".join(value) + spaceb + " |")
    if(len(table) == 3):
        return("""------------------
|  time | items  |
------------------
| No items found |
------------------
""")
    table.append("-" * (longa + longb + 7))
    if x:
        spaceb = " " * (longb - len("items") + 1)
        table[-1] = ("-" * (longa + longb + 6))
        table[1] = ("|    " + "time | items" + spaceb + "|")
    return "\n".join(table)


def get_table_sizes(dict: dict):
    """Get the maximum sizes for table."""
    if len(dict.items()) < 1:
        return 4, 5
    longa = max(len(x) for x in dict.keys())
    longb = max(len(", ".join(x)) for x in dict.values())
    if longa < 4:
        longa = 4
    if longb < 5:
        longb = 5
    return longa, longb


def normalize(a: dict):
    """Add missing 0's to the minutes and remove extra 0's from hours."""
    b = {}
    result = {}
    count = 0
    for key, value in a.items():
        b[key] = value
    for key in a.keys():
        f = datetime.strptime(key, "%H:%M")
        correct = (f.strftime("%I:%M %p"))
        b[correct] = b[key]

    for key in b.keys():
        if count >= len(a.keys()):
            key2 = key
            if key[0] == "0":
                lis = list(key)
                lis[0] = " "
                key2 = "".join(lis)
            result[key2] = b[key]
        count += 1
    return result


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_text = str
    with open(input_filename, 'r') as filehandle:
        input_text = filehandle.read()
    result = create_schedule_string(input_text)
    with open(output_filename, 'w') as file:
        file.write(result)


if __name__ == '__main__':
    # "24:00 tere wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst 9:00 test 8:59 a 25:05 laps 24:05 laps2 23:05 laps3 22:05 laps4"
    print(create_schedule_string("1:1 a 1:2 b 1:3 c 1:4 aaa"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")