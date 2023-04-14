#!/usr/bin/python3

'''
program
'''


def displayOutput(statuses, sizes):
    '''The function outputs size and status occurrences count'''
    sizes = [int(i) for i in sizes]
    sizes_sum = sum(sizes)
    print(f"File size: {sizes_sum}")
    my_set = set(statuses)
    for status in sorted(my_set):
        occurence = statuses.count(status)
        print(f'{status}: {occurence}')