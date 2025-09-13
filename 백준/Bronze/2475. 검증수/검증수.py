import sys


def b2475(N:list):
    result = 0
    for i in N:
        result += i*i
    return result %10

if __name__ == '__main__':
    sys.stdout.write(str(b2475(list(map(int, sys.stdin.readline().split())))))