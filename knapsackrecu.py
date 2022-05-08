def knapsack(i,j,val,w):
	table = [[0 for x in range(i+1)]for x in range(j+1)]
	if i == 0:
		return table[i][j]=0
	else:
		for u in j:
			table[i][u] = max(knapsack(i-1,u,val,w)+val[i-1],knapsack(i-1,u,val,w))
	