def maxA(self, N):
	dp = collections.defaultdict(lambda : collections.defaultdict(int))
	dp[0][0] = 0
	for z in range(N):
		for y in dp[z]:
			#Key 1: (A):
            dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)
            #Key 4: (Ctrl-V):
            dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)
            #Key 2: (Ctrl-A): + Key 3: (Ctrl-C):
            dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])
    return max(dp[N].values())