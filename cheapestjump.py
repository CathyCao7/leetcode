def cheapestJump(self, A, B):
	N = len(A)
	cost = [0x7FFFFFFF] * (N + 1)
	cost[1] = A[0]
	path = [[] for x in range(N + 1)]
	path[1] = [1]
	for x in range(2, N+1):
		if A[x-1] == -1: continue
		for y in range(1, B+1):
			z = x - y
			if z < 1: break
			if A[z-1] == -1: continue
			if cost[x] > cost[z] + A[x - 1] or cost[x] == cost[z] + A[x - 1] and path[x] > path[z] + [x]:
                cost[x] = cost[z] + A[x - 1]
                path[x] = path[z] + [x]
    return path[-1]