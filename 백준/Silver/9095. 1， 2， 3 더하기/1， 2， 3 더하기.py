import sys

# 미리 DP 테이블을 계산해 둔다 (n의 최대값은 10이므로 11까지 계산)
dp = [0] * 12
dp[1] = 1  # 1
dp[2] = 2  # 1+1, 2
dp[3] = 4  # 1+1+1, 1+2, 2+1, 3

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 테스트 케이스 처리
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    sys.stdout.write(str(dp[num]) + '\n')