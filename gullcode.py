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

    if n is 2:
        return True
    elif n % 2 is 0 or n is 1:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i is 0:
            return False

    return True


def nth_prime(n: int) -> int:
    # Comment out if program gets too slow
    assert (type(n) == int), 'Argument must be integer.'

    p = 1
    i = 1
    while True:
        if is_prime(i):
            p += 1
        if p == n:
            return i
        i += 2


if __name__ == '__main__':
    print(nth_prime(6969))
