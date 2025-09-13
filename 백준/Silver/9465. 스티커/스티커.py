# Number of test cases
T = int(input())  # Read the number of test cases

for _ in range(T):
    n = int(input())  # Number of columns (stickers per row)

    # Read both sticker rows
    stickers = [list(map(int, input().split())) for _ in range(2)]

    # Initialize dp table with 0
    dp = [[0]*n for _ in range(2)]  # Create 2xN dp table

    # Base case for column 0
    dp[0][0] = stickers[0][0]  # Top row first column
    dp[1][0] = stickers[1][0]  # Bottom row first column

    if n > 1:
        # Base case for column 1
        dp[0][1] = dp[1][0] + stickers[0][1]  # Choose (0,1), previous (1,0)
        dp[1][1] = dp[0][0] + stickers[1][1]  # Choose (1,1), previous (0,0)

    for i in range(2, n):
        # Choose (0,i), check max of (1,i-1) and (1,i-2)
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]

        # Choose (1,i), check max of (0,i-1) and (0,i-2)
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]

    # Output the best value of the last column
    print(max(dp[0][n-1], dp[1][n-1]))
