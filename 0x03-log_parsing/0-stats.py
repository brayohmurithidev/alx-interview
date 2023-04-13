#!/usr/bin/python3

'''
A program that takes in standard input.
It spits file size and number of status code occurences
'''

import re
import sys

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


'''The code sets a condition that needs to be met.'''
try:
    while True:
        name = sys.stdin.readline()
        match = check_pattern_match(format_pattern, name)
        if match is not False:
            names.append(name)
            input_count += 1
            if input_count % 10 == 0:
                display_output(status_codes, total_sizes)

except KeyboardInterrupt:
    display_output(status_codes, total_sizes)
