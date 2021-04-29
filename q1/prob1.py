# Justin Ventura & Jacob Duncan Gull Code 2021
import sys
# every 5
def get_zeroes(n):
    res = 0
    for i in range(5, n+1, 5):
        j=i
        while j % 5 == 0:
            j /= 5
            res += 1
    return res

if __name__ == '__main__':
    N = int(sys.stdin.read())
    print(get_zeroes(N))
