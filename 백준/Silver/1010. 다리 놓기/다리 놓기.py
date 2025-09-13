import math
import sys


def B1010(N:int, M:int):
    return int(math.factorial(M)/(math.factorial(N)*math.factorial(M-N)))

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        sys.stdout.write(str(B1010(N,M)) + '\n')