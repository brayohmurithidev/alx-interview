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

def display_output(statuses, sizes):
    '''The function outputs size and status occurrences count'''
    sizes = [int(i) for i in sizes]
    sizes_sum = sum(sizes)
    print(f"File size: {sizes_sum}")
    my_set = set(statuses)
    for status in sorted(my_set):
        occurence = statuses.count(status)
        print(f'{status}: {occurence}')


