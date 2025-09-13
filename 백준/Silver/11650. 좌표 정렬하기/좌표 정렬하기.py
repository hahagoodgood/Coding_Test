import sys

N = int(sys.stdin.readline())
coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# x 좌표를 기준으로 정렬하고, x 좌표가 같으면 y 좌표를 기준으로 정렬
coordinates.sort()

for x, y in coordinates:
    print(x, y)
