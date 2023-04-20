#!/usr/bin/python3

"""This script reads input from standard input line by
line and computes some statistics"""

import sys


def print_statistics(status_codes, total_size):
    """Prints statistics for the input data"""
    print("Total file size: {:d}".format(total_size))
    for status, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {:d}".format(status, count))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

count = 0
total_size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_statistics(status_codes, total_size)

        fields = line.split()
        count += 1

        try:
            size = int(fields[-1])
            total_size += size
        except ValueError:
            pass

        try:
            status_code = fields[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except IndexError:
            pass

    print_statistics(status_codes, total_size)

except KeyboardInterrupt:
    print_statistics(status_codes, total_size)
    raise
