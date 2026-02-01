N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

# Round-up division: (item + T - 1) // T
t_set = sum((item + T - 1) // T for item in size)

print(t_set)
print(N // P, N % P)