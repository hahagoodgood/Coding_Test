import sys
def B26529(x:int):
    if x<=1:
        return 1
    else:
        dp = [0]*(x+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, x+1): dp[i] = dp[i-1]+dp[i-2]
        return dp[x]



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        sys.stdout.write(str(B26529(int(sys.stdin.readline())))+'\n')
