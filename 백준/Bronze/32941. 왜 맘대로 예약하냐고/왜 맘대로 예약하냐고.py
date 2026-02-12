T, X = map(int, input().split())
N = int(input())
result = "YES"

for i in range(N):
    scd_cnt = int(input())
    schedule = list(map(int, input().split()))
    if X not in schedule :
        result = "NO"

print(result)