import heapq  # For priority queue
import sys

# Read multiple test cases
T = int(sys.stdin.readline())  # Number of test cases

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())  # Number of nodes, edges
    graph = [[] for _ in range(N + 1)]  # Adjacency list

    # Input for M edges
    for _ in range(M):
        u, v, cost = map(int, sys.stdin.readline().split())  # Undirected edge
        graph[u].append((v, cost))  # Add edge u->v
        graph[v].append((u, cost))  # Add edge v->u

    K = int(sys.stdin.readline())  # Number of friends
    friends = list(map(int, sys.stdin.readline().split()))  # Starting nodes

    # Function: Dijkstra's Algorithm
    def dijkstra(start):
        dist = [float('inf')] * (N + 1)  # Initialize distances
        dist[start] = 0  # Distance to self is 0
        hq = [(0, start)]  # Priority queue

        while hq:
            cost, now = heapq.heappop(hq)  # Pop node with smallest cost

            if cost > dist[now]:
                continue  # Already visited with shorter path

            for neighbor, weight in graph[now]:
                if dist[neighbor] > cost + weight:
                    dist[neighbor] = cost + weight  # Update distance
                    heapq.heappush(hq, (dist[neighbor], neighbor))  # Push neighbor

        return dist  # Return distances from 'start'

    # distances[i]: i번째 친구가 각 노드까지 가는 최소 거리
    distances = [dijkstra(friend) for friend in friends]

    min_total_distance = float('inf')  # Initialize minimum sum
    best_node = 0  # Best meeting node

    # For each node 1~N, sum distances from all friends
    for i in range(1, N + 1):
        total = 0  # Total distance to node i
        for dist in distances:
            total += dist[i]  # Add distance from a friend
        if total < min_total_distance:  # If smaller total found
            min_total_distance = total
            best_node = i  # Update best node

    print(best_node)  # Print result
