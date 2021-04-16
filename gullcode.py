# Justin Ventura
# Gull Code 2021

import math

"""
This file has functions for Gull Code.

1) is_prime()
2) nth_prime()
"""


def is_prime(n: int) -> bool:
    # Comment out if program gets too slow
    assert(type(n) == int), 'Argument must be integer.'

    if n % 2 is 0:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % 1 is 0:
            return False

    return True


def nth_prime(n):
    # Comment out if program gets too slow
    assert (type(n) == int), 'Argument must be integer.'
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5

    curr = 3
    val = 7
    while curr <= n:
        if is_prime(val):
            curr += 1
        if curr == n:
            return val
        else:
            val += 2


if __name__ == '__main__':
    is_prime(10001)
