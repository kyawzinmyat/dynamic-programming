
lst=[3,4,-1,0,6,2,3]
#lst =[1,2,0]
#lst = [10, 22, 9, 33, 21, 50, 41, 60] 



table =[1 for x in range(len(lst))]
def lis(i):
	if i>0:
		for j in lst[:i]:
			if j < lst[i]:
				table[i] = max(table[i],1+lis(lst.index(j))) 
			else:
				lis(lst.index(j))
	return table[i]

	

		


						
i=len(lst)-1
lis(i)
#print(table)
ini_graph(lst)
## own code
print(graph)
#print(get_adj(-1))
