import sys

n = int(input())
INF = 10000000
dp = [INF] * (100000 + 1)
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i], dp[i - 2] + 1, dp[i - 5] + 1)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])