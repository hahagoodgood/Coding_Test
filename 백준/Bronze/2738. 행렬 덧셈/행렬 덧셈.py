import sys

N, M = map(int, sys.stdin.readline().split())
list_1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for idx in range(N):
    result = " ".join(str(x+y) for x, y in zip(list_1[idx], list_2[idx]))
    sys.stdout.write(result + "\n")
