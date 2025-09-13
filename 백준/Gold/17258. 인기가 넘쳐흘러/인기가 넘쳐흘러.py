n, m, k, t = map(int, input().split())
a = [0] * 301
for _ in range(m):
    a_, b_ = map(int, input().split())
    for i in range(a_, b_):
        a[i] = min(t, a[i] + 1)

v = []
temp = a[1]
_count = 1
for i in range(2, n + 1):
    if temp != a[i]:
        v.append((_count, temp))
        _count = 0
        temp = a[i]
    _count += 1
v.append((_count, temp))

dp = [[0] * 301 for _ in range(301)]

def go(here, num, prev):
    if here == len(v):
        return 0
    if dp[here][num] != 0:
        return dp[here][num]

    cost = max(0, t - v[here][1])
    real_cost = 0 if prev >= cost else cost

    ret = dp[here][num]
    if num - real_cost >= 0:
        ret = max(go(here + 1, num - real_cost, cost) + v[here][0], go(here + 1, num, 0))
    else:
        ret = go(here + 1, num, 0)
    
    dp[here][num] = ret
    return ret

print(go(0, k, 0))
