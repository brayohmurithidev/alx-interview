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


    def check_pattern_match(pattern, userInput):
        '''
        The function checks user input against the pattern
        '''
        match = re.match(pattern, userInput)
        if not match:
            print('did not meet pattern')
            return False
        else:
            total_size = match.group(4)
            total_sizes.append(total_size)
            status_code = match.group(3)
            status_codes.append(status_code)


    def display_output(statuses, sizes):
        '''The function outputs size and status occurrences count'''
        sizes = [int(i) for i in sizes]
        sizes_sum = sum(sizes)
        print(f"File size: {sizes_sum}")
        my_set = set(statuses)
        for status in sorted(my_set):
            occurence = statuses.count(status)
            print(f'{status}: {occurence}')
