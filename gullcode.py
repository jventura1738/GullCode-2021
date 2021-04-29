# Justin Ventura
# Gull Code 2021

import math
import numpy as np

"""
This file has functions for Gull Code.

1) is_prime()
2) nth_prime()
3) regression()
"""


def is_prime(n: int) -> bool:
    # Comment out if program gets too slow
    # assert(type(n) == int), 'Argument must be integer.'

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
    # assert (type(n) == int), 'Argument must be integer.'

    p = 1
    i = 1
    while True:
        if is_prime(i):
            p += 1
        if p == n:
            return i
        i += 2


def _loss(alpha, beta, xi, yi):
    return xi*beta + alpha - yi


def _step(start, grad, rate):
    return np.array(start) - np.array(grad) * rate


def regression(xys):
    iters = 10000
    gamma = 0.001
    alpha, beta = 0, 1

    for _ in range(iters):
        grad_b = np.sum([2 * xi * _loss(alpha, beta, xi, yi) for (xi, yi) in xys])
        grad_a = np.sum([2 * _loss(alpha, beta, xi, yi) for (xi, yi) in xys])
        res = _step([alpha, beta], [grad_a, grad_b], gamma)
        alpha, beta = res

    return [alpha, beta]


if __name__ == '__main__':
    s = [(i,3*i+ 4) for i in range(0,10)]
    print(regression(s))