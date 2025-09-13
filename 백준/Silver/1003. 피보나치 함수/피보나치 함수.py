import sys
def B1003(n:int):

    if n == 0:
        return f"1 0"
    # elif n == 1:
    #     return f"0 1"
    else:
        # dp 테이블 초기화
        dp = [[0,0]]*(n+1)
        dp[0] = [1,0]
        dp[1] = [0,1]
        # 피보나치의 n의 0과 1의 호출 개수 -> n-1 과 n-2의 갯수의 합
        for i in range(2,n+1):
            dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
        return f"{dp[n][0]} {dp[n][1]}"
if __name__ == "__main__":
    testcase = int(sys.stdin.readline())
    for _ in range(testcase):
        sys.stdout.write(B1003(int(sys.stdin.readline()))+"\n")
