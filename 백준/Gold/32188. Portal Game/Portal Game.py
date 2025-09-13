from collections import deque
import sys

def clear_game(n, c, portal_info):
    portal_list = [None]*n
    list = [float('inf')] * n


    for color, start, end in portal_info:
        portal_list[start] = (color, end)

    queue = deque()
    queue.append((0, 0))
    list[0] = 0

    while queue:
        current, time = queue.popleft()

        if portal_list[current]:
            color, dest = portal_list[current]
            if list[dest] > time:
                list[dest] = time
                queue.appendleft((dest, time))
            if color == 1 and current + 1 < n and list[current+1] > time+1 :
                list[current + 1] = time + 1
                queue.append((current + 1, time + 1))
        else:
            if current + 1 < n and list[current + 1] > time+1:
                list[current + 1] = time+1
                queue.append((current + 1, time + 1))

    return list[n - 1] if list[n - 1] < float('inf') else -1

input = sys.stdin.readline
n, c = map(int, input ().split())
portal_info = [tuple(map(int, input().split())) for _ in range(c)]
print(clear_game(n, c, portal_info))