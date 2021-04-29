# Justin Ventura

import sys

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')
    N, M = map(int, lines[0])
    l = 0
    for i in range(M):
        l = tuple(map(int, lines[i+1]))
