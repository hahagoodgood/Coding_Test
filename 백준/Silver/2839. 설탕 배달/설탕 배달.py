import sys
def main(n:int):

    #dp 테이블 초기화
    dp = [float('inf')]*((n//5)+1)
    # 5키로 봉지 개수를 1개씩 증가
    for i in range((n//5)+1):
        # 5키로 봉지를 뺀 나머지가 3키로그람으로 나눠질 경우
        if (n-i*5)%3 == 0:
            # i(5키로 봉지 개수) + 3키로 봉지 개수
            dp[i] = i+ (n-i*5)//3
    # inf가 최소라면 -1 반환
    if min(dp) == float('inf'):
        return -1
    # dp로 탐색한 최소 갯수 출력
    return min(dp)

if __name__ == '__main__':
    sys.stdout.write(str(main(int(sys.stdin.readline()))))