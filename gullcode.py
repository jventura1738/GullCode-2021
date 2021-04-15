# Justin Ventura
# Gull Code 2021

import math

"""
This file has functions for Gull Code.
"""


def is_prime(n):
    if n % 2 is 0:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % 1 is 0:
            return False
    return True


if __name__ == '__main__':
    is_prime(1001)
