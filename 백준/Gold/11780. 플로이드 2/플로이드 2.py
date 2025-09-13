import sys
input = sys.stdin.readline

# Read number of cities
n = int(input())  # Number of nodes
m = int(input())  # Number of edges

INF = float('inf')  # Infinity value

# Initialize distance and route arrays
dist = [[INF] * (n + 1) for _ in range(n + 1)]  # Distance matrix
route = [[0] * (n + 1) for _ in range(n + 1)]   # Route tracking matrix

# Set distance to self as 0
for i in range(1, n + 1):
    dist[i][i] = 0  # Distance to self is zero

# Read bus connections
for _ in range(m):
    u, v, cost = map(int, input().split())
    if cost < dist[u][v]:  # Take the minimum cost if multiple edges exist
        dist[u][v] = cost
        route[u][v] = v  # Direct path from u to v

# Floyd-Warshall algorithm
for k in range(1, n + 1):  # Intermediate node
    for i in range(1, n + 1):  # Start node
        for j in range(1, n + 1):  # End node
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                route[i][j] = route[i][k]  # Update route

# Print the shortest distance matrix
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(0, end=' ')  # If no path exists
        else:
            print(dist[i][j], end=' ')
    print()

# Function to reconstruct path from i to j
def get_path(i, j):
    if route[i][j] == 0:
        return []  # No path
    path = [i]
    while i != j:
        i = route[i][j]
        path.append(i)
    return path

# Print the paths
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF or i == j:
            print(0)
        else:
            path = get_path(i, j)
            print(len(path), *path)
