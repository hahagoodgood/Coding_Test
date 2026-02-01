N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

# Calculate minimum T-shirt bundles needed
t_set = 0
for item in size:
    # If remainder exists, need one extra bundle; otherwise exact division
    t_set += (item // T + 1) if item % T else item // T

print(t_set)
print(str(N // P) + " " + str(N % P))