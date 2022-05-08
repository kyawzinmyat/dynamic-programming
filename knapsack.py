
def knapsack(aw,w,val):
	n = len(val)
	table = [[0 for x in range(aw+1)]for x in range(n+1)]
	
	for i in range(n+1):
		for j in range(0,aw+1):
			if i==0 or j ==0:
				table[i][j] =0
			elif w[i-1]<=j:
				table[i][j] = max(val[i-1]+table[i-1][j-w[i-1]],table[i-1][j])
			else:
				table[i][j] = table[i-1][j]
	return table[i][j]
		




		

val = [50,100,150,200]
w = [8,16,32,40]
aw = 64
n=4
print(knapsack(aw,w,val))