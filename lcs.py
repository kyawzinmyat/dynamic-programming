l1 =['n','e','n']
l2 =['o','e','n']

table =[[0 for x in range(len(l1)+1)]for j in range(len(l2)+1)]

def lcs(i,j):
	if i ==0 or j ==0:
		return 0

	if l1[i-1] == l2[j-1]:	
		table[i][j]= 1 + lcs(i-1,j-1)
		return table[i][j]
	else:
		table[i][j]= max(lcs(i-1,j),lcs(i,j-1))
		return table[i][j]
		
		

	
i = len(l1)
j = len(l2)
print(lcs(i,j))
#print(get_lcs(table,i,j))
print(table)	

	