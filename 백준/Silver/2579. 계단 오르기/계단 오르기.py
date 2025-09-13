n = int(input())
inputs = [0]
for i in range(n):
    inputs.append(int(input()))

if n == 1:
    print(inputs[1])
else :
    # 각 계단에서 얻을 수 있는 최고 점수를 기록한다.
    dp = [0]*(n+1)
    dp[1] = inputs[1]
    dp[2] = inputs[1]+inputs[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + inputs[i-1]) + inputs[i]

    print(dp[n])