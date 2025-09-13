import sys


def B9655(N:int):
    if N <= 3 :
        if N%2 == 1 :return 'SK'
        else: return 'CY'
    else:
        dp = ['']*(N+1)
        dp[1] ='SK'
        dp[2] = 'CY'
        dp[3] = 'SK'
        dp[4] = 'CY'
        for i in range(5,N+1):
            if dp[i-1] == 'CY' or dp[i-3] == 'CY':
                dp[i] = 'SK'
            else:
                dp[i] = 'CY'
        return dp[N]

if __name__ == '__main__':
    sys.stdout.write(B9655(int(sys.stdin.readline())))