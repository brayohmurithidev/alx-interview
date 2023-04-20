#!/usr/bin/python3

"""
File that represents a given data set to a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    function that determine if a given data set
    represents a valid UTF-8 encoding.
    """
    bytes_remaining = 0

    for byte in data:
        if bytes_remaining == 0:
            if byte >> 7 == 0b0:
                bytes_remaining = 0
            elif byte >> 5 == 0b110:
                bytes_remaining = 1
            elif byte >> 4 == 0b1110:
                bytes_remaining = 2
            elif byte >> 3 == 0b11110:
                bytes_remaining = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                bytes_remaining -= 1
            else:
                return False
    if bytes_remaining > 0:
        return False
    return True
