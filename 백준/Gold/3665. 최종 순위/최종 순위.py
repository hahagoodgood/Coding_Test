import sys
from collections import deque

input = sys.stdin.readline

def solve():
    T = int(input())  
    for _ in range(T):
        n = int(input())

        last_year = list(map(int, input().split()))

        graph = [[False] * (n + 1) for _ in range(n + 1)]
        indegree = [0] * (n + 1)

        for i in range(n):
            for j in range(i + 1, n):
                high = last_year[i]
                low = last_year[j]
                graph[high][low] = True
                indegree[low] += 1

        m = int(input())  

        for _ in range(m):
            a, b = map(int, input().split())
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indegree[b] -= 1
                indegree[a] += 1
            else:
                graph[b][a] = False
                graph[a][b] = True
                indegree[a] -= 1
                indegree[b] += 1

        q = deque()
        result = []

        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)

        certain = True
        cycle = False 

        for _ in range(n):
            if not q:
                cycle = True
                break
            if len(q) > 1:
                certain = False
            now = q.popleft()
            result.append(now)
            for j in range(1, n + 1):
                if graph[now][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)

        if cycle:
            print("IMPOSSIBLE")
        elif not certain:
            print("?")
        else:
            print(' '.join(map(str, result)))

solve()