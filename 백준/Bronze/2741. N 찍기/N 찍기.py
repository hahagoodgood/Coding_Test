import sys


def b2475(N:int):
    for i in range(1,N+1):
        sys.stdout.write(str(i) + '\n')

if __name__ == '__main__':
    b2475(int(sys.stdin.readline()))