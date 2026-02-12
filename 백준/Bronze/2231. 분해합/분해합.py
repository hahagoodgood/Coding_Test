N = int(input())
result = 0
for i in range(max(1, N - 63), N):
    if i + sum(map(int, str(i))) == N:
        result = i
        break
print(result)
