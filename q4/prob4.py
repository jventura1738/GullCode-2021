# Justin Ventura, Jacob Duncan, Blaine Mason

import sys

def rotate(s, i):
    return s[len(s) - i:] + s[0: len(s) - i]

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')
    N, binary = int(lines[0]), lines[1]
    mat = [rotate(binary, j) for j in range(N)]
    print(mat[-1])

