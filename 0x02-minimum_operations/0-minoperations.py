#!/usr/bin/env python3

'''
A function to return minimum number of operation to carry out
copy all and paste operations
'''


def minOperations(n):
    '''
    The function takes the least common factor of the given number
    '''
    if (n < 2):
        return 0
    factors = []
    divisor = 2
    while (n >= 2):
        # check if n is divisible by 2
        if (n % divisor == 0):
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    return sum(factors)
