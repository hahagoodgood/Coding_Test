import heapq  # Priority queue for BFS

# Input
n, m = map(int, input().split())  # Map size (rows, cols)
sx, sy, ex, ey = map(int, input().split())  # Start and end positions
graph = [list(input().strip()) for _ in range(n)]  # Read map

# Adjust to 0-index
sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1  # Change to 0-index

# Directions: up, down, left, right
dx = [-1, 1, 0, 0]  # x-axis movement
dy = [0, 0, -1, 1]  # y-axis movement

# Initialize visited map with large value
visited = [[float('inf')] * m for _ in range(n)]  # Store minimum break count
visited[sx][sy] = 0  # Starting point cost is 0

# Priority Queue: (break_count, x, y)
q = []
heapq.heappush(q, (0, sx, sy))  # Start from initial point

# BFS with priority queue (Dijkstra-style)
while q:
    count, x, y = heapq.heappop(q)  # Get current position

    if x == ex and y == ey:  # If reached destination
        print(count+1)  # Output result
        break

    for i in range(4):  # Check 4 directions
        nx = x + dx[i]  # Next x
        ny = y + dy[i]  # Next y

        if 0 <= nx < n and 0 <= ny < m:  # Check boundary
            # Add 1 if wall, else 0
            cost = count + (1 if graph[nx][ny] == '1' else 0)  # Add cost if wall
            if visited[nx][ny] > cost:  # If this path is better
                visited[nx][ny] = cost  # Update visited with better cost
                heapq.heappush(q, (cost, nx, ny))  # Push to queue