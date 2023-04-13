#!/usr/bin/env python3

'''

'''

import re

format_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'

names = []
input_count = 0
total_sizes = []
status_codes = []

def check_pattern_match(pattern, userInput):
    match = re.match(pattern, userInput)
    if not match:
        print('did not meet pattern')
        return False
    else:
        total_size = match.group(4)
        total_sizes.append(total_size)
        status_code = match.group(3)
        status_codes.append(status_code)


# DISPLAY 
def display_output(statuses, sizes):
    sizes = [int(i) for i in sizes]
    sizes_sum = sum(sizes)
    print(f"File size: {sizes_sum}")
    my_set = set(statuses)
    for status in sorted(my_set):
        occurence = statuses.count(status)
        print(f'{status}: {occurence}')



try:
    while True:
        name = input("Input url: ")
        match = check_pattern_match(format_pattern, name)
        if  match != False:
            names.append(name)
            input_count += 1
            print(input_count)
            if(input_count == 5):
                display_output(status_codes, total_sizes)

except KeyboardInterrupt:
    display_output(status_codes, total_sizes)