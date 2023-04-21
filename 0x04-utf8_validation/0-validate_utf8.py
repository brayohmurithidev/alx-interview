#!/usr/bin/python3

"""
File that represents a given data set to a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    Return True if data is a valid
    UTF-8 encoding, else return False.
    A character in UTF-8 can be 1 to 4 bytes long.
    The data set can contain multiple characters.
    The data will be represented by a list of integers.
    Each integer represents 1 byte of data,
    therefore you only need to handle the 8 least
    significant bits of each integer.
    """
    num_bytes = 0  # Number of bytes in the current UTF-8 character
    mask1 = 1 << 7  # Masks for checking if byte is valid (starts with 10)
    mask2 = 1 << 6

    for byte in data:
        mask_n_byte = 1 << 7

        if num_bytes == 0:
            # Count number of bytes the UTF-8 Character will have
            while mask_n_byte & byte:
                num_bytes += 1
                mask_n_byte = mask_n_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Every byte that is not the first byte of a character should start
            # with 10, otherwise is not valid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
