import sys
INF = 100001
def b14916(n:int):
    # if n <=4 :
    #     if n % 2 == 0:
    #         return n//2
    #     return -1
    # else:
    #     dp = [[0,0]]*(n+1)
    #     dp[1] = [0, 0]
    #     dp[2] = [1, 0]
    #     dp[3] = [0, 0]
    #     dp[4] = [2, 0]
    #     dp[5] = [0, 1]
    #     for i in range(6,n+1):
    #         if dp[i - 5] != [0, 0]: dp[i] = [dp[i - 5][0], dp[i - 5][1] + 1]
    #         elif dp[i-2] != [0,0]: dp[i] = [dp[i-2][0]+1, dp[i-2][1]]
    #         else: return -1
    #     return sum(dp[n])
    dp = [INF] * (n + 1 if n > 5 else 6)
    dp[0] = 0
    for i in range(1, n+1):
        if i>=2 and dp[i-2] != INF:
            dp[i] = min(dp[i-2] + 1, dp[i])
        if i>=5 and dp[i-5] != INF:
            dp[i] = min(dp[i-5]+1, dp[i])

    if dp[n] == INF:
        return -1
    return dp[n]

if __name__ == '__main__':
    sys.stdout.write(str(b14916(int(sys.stdin.readline()))))