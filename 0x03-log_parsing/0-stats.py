#!/usr/bin/python3

"""
This module reads input from standard input and looks for lines that match a specific pattern.

The pattern is defined as a regular expression in the variable `format_pattern`. Each line of
input is checked against the pattern, and if it matches, the status code and total size are
extracted and added to `status_codes` and `total_sizes`, respectively.

Every 10 input lines, the function `display_output()` is called to output the total file size and
a count of occurrences for each status code.

To use this module, simply pipe input into the script and it will automatically process the input
and output the results.
"""

import re
import sys


def readStdin():
    '''Main function'''
    format_pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '\
    r'"GET /projects/\d+ HTTP/1\.1" (\d+) (\d+)$'
    names = []
    input_count = 0
    total_sizes = []
    status_codes = []

    try:
        while True:
            url = sys.stdin.readline()
            match = re.match(format_pattern, url)
            if match:
                 names.append(url)
                 input_count += 1
                 if input_count % 10 == 0:
                     print(names)



    except KeyboardInterrupt:
        print(names)
        raise


if __name__ == '__main__':
    result = readStdin()
    print(result)