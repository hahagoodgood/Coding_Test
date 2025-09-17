import sys

def b10250(h:int, w:int, n:int):
    col = (n-1)%h+1
    row = (n-1)//h+1
    return f"{col}{row:02d}"


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        sys.stdout.write(b10250(*list(map(int,sys.stdin.readline().split()))[:3])+'\n')