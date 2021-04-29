# Justin Ventura & Blaine Mason

"""
Question 3
"""
import sys

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')
    n, m, k = map(int, lines[0].split())
    bad_squares = []
    for i in range(k):
        bad_squares.append(tuple(map(int, lines[i+1].split())))

    print(bad_squares)


