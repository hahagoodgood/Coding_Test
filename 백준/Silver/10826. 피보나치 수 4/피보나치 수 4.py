import sys


def b10826(n:int):
    dp = [0]*(2 if n < 2 else n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

if __name__ == '__main__':
    sys.stdout.write(str(b10826(int(sys.stdin.readline()))))
