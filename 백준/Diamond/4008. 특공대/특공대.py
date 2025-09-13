import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
a, b, c = map(int, input().split())
nums = list(map(int, input().split()))

psum = [0] * (N + 1)
for i in range(N):
    psum[i + 1] = psum[i] + nums[i]

dp = [float('-inf')] * (N + 1)
dp[0] = 0

def get_dp(j, s):
    return dp[j] + a * (s - psum[j]) * (s - psum[j]) + b * (s - psum[j]) + c


def get_line_coefficient(j):
    return (-2 * a * psum[j], dp[j] + a * psum[j] * psum[j] - b * psum[j])


def get_intersection(i, j):
    m1, n1 = get_line_coefficient(i)
    m2, n2 = get_line_coefficient(j)
    if m1 == m2:
        return float('inf') if n1 >= n2 else float('-inf')
    return (n2 - n1) / (m1 - m2)


dq = deque([0])

for i in range(1, N + 1):
    while len(dq) > 1 and get_dp(dq[0], psum[i]) <= get_dp(dq[1], psum[i]):
        dq.popleft()

    j = dq[0]
    dp[i] = get_dp(j, psum[i])

    while len(dq) > 1:
        j1 = dq[-2]
        j2 = dq[-1]

        if get_intersection(j1, i) <= get_intersection(j1, j2):
            dq.pop()
        else:
            break

    dq.append(i)

print(dp[N])