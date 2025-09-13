n, m = map(int,input().split())
a = [0 for i in range(n)]
for i in range(m):
    i,j,k = map(int,input().split())
    for i in range(i-1,j):
        a[i] = k
for i in range(n):
    print(a[i], end=" ")