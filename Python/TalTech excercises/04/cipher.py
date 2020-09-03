"""Encode and decode text using Rail-fence Cipher."""

def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    # replace spaces with _
    message = message.replace(" ", "_")
    # key = rows
    # len(message) = columns
    # creating the rail matrix
    rail = [['\n' for i in range(len(message))]
            for j in range(key)]
    # to find the direction
    dir_down = False
    row, col = 0, 0
    if key != 1:
        for i in range(len(message)):
            # check the direction, reverse it
            # if just filled the top or bottom rail
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
            # fill the corresponding alphabet
            rail[row][col] = message[i]
            col += 1
            # go to next row, according to dir
            if dir_down:
                row += 1
            else:
                row -= 1
        # now construct the cipher
        # using the rail matrix
        result = []
        for i in range(key):
            for j in range(len(message)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return("".join(result))
    else:
        return message


def getResult(message, key, rail):
    """Read the matrix and get result."""
    result = []
    row, col = 0, 0
    for i in range(len(message)):
        # check the dir
        if row == 0:
            dir_down = True
        if row == (key - 1):
            dir_down = False
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return result


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    # replace _ with space
    message = message.replace("_", " ")
    # key = rows
    # len(message) = columns
    if key != 1:
        # create rail
        rail = [['\n' for i in range(len(message))]
                for j in range(key)]
        # find the direction
        dir_down = None
        row, col = 0, 0
        # mark the places with *
        for i in range(len(message)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            # place the marker
            rail[row][col] = '*'
            col += 1
            # find the next row
            # using dir
            if dir_down:
                row += 1
            else:
                row -= 1
        # fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(message)):
                if ((rail[i][j] == '*') and (index < len(message))):
                    rail[i][j] = message[index]
                    index += 1
        # now read the matrix and get result
        result = getResult(message, key, rail)
        return("".join(result))
    else:
        return message