#!/usr/bin/python3

"""
File that represents a given data set to a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    :param data: a list of integers representing the bytes of the data set
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    # Keep track of the number of bytes remaining in the current character
    bytes_remaining = 0

    # Iterate through each byte in the data set
    for byte in data:
        # Check if this byte is the start of a new character
        if bytes_remaining == 0:
            # Determine the number of bytes in this character
            if byte >> 7 == 0b0:
                # Character is 1 byte long
                bytes_remaining = 0
            elif byte >> 5 == 0b110:
                # Character is 2 bytes long
                bytes_remaining = 1
            elif byte >> 4 == 0b1110:
                # Character is 3 bytes long
                bytes_remaining = 2
            elif byte >> 3 == 0b11110:
                # Character is 4 bytes long
                bytes_remaining = 3
            else:
                # Invalid start byte
                return False
        else:
            # This byte is a continuation byte
            if byte >> 6 == 0b10:
                # This is a valid continuation byte
                bytes_remaining -= 1
            else:
                # This is an invalid continuation byte
                return False

    # If there are still bytes remaining in the current
    # character, the data set is invalid
    if bytes_remaining > 0:
        return False

    # If we made it through the whole data set without
    # finding any errors, it is valid UTF-8
    return True
