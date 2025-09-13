import sys
def B1453(n:int):
    #dp 테이블 초기화
    dp = [0]*(n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        # 2으로만 나눠질 때
        if i%3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        # 2로만 나누질 때
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
    return dp[n]

if __name__ == '__main__':
    sys.stdout.write(str(B1453(int(sys.stdin.readline()))))