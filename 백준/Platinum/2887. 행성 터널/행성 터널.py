import sys  # For fast input
input = sys.stdin.readline

# Disjoint Set (Union-Find) 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root

# Read number of planets
n = int(input())

# 행성 좌표 저장 (번호 포함)
planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((i, x, y, z))  # (index, x, y, z)

edges = []

# x축 기준 정렬 후 인접 노드 간선 저장
planets.sort(key=lambda p: p[1])
for i in range(n - 1):
    a, ax, _, _ = planets[i]
    b, bx, _, _ = planets[i + 1]
    cost = abs(ax - bx)
    edges.append((cost, a, b))

# y축 기준 정렬 후 인접 노드 간선 저장
planets.sort(key=lambda p: p[2])
for i in range(n - 1):
    a, _, ay, _ = planets[i]
    b, _, by, _ = planets[i + 1]
    cost = abs(ay - by)
    edges.append((cost, a, b))

# z축 기준 정렬 후 인접 노드 간선 저장
planets.sort(key=lambda p: p[3])
for i in range(n - 1):
    a, _, _, az = planets[i]
    b, _, _, bz = planets[i + 1]
    cost = abs(az - bz)
    edges.append((cost, a, b))

# 간선 비용 기준 정렬
edges.sort()

# Union-Find 초기화
parent = [i for i in range(n)]
result = 0  # 최소 비용 합

# 크루스칼 알고리즘
for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

# 최종 결과 출력
print(result)
