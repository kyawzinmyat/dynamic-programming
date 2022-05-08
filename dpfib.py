
def fib_(num):## exponential
	global i
	i+=1
	print('fib_ called with',i)
	if 0<num<=2:
		return 1
	else:
		return fib(num-1)+fib(num-2)
	
	
table={1:1,2:1}		
		
def fib(num):
	global i
	i+=1
	print('fib called with',i)
	if check(num):
		return check(num)
	else:		
		return fib(num-1)+fib(num-2)
		

def fib2(num):
	global i
	i+=1
	print('fib2 called with',i)
	if not num in table:
			table[num]=fib2(num-1) + fib2(num-2)
	return table[num]		

	
def check(num):
	table ={
					1:1,
					2:1
				}
	if num in table:
		return table[num]
i=0
#print(fib(10))
#print(fib_(10))
print(fib2(9))
#print(table)
def knap(value,weight,size):
	bag =[[0 for x in range(size+1)]for i in range(len(value))]
	for i in range(0,len(value)):
		for j in range(size+1):
			if i == 0 or j == 0:
				bag[i][j]=0
			elif weight[i-1]<=size:
				bag[i][j]=max(value[i-1]+bag[i-1][j-weight[i-1]],bag[i][j])
			#	pass
			else:
				bag[i][j]=bag[i-1][j]
#	print(bag)
	
#print(knap([4,3,2,1],[1,1,1,1],5))



def fib_loop(num):# linear time
	temp=[1,1]
	for i in range(1,num+1):
		if i<=2:
			pass
		else:
			ans = temp[0]+temp[1]
			temp[0],temp[1]=temp[1],ans
	return ans		
print(fib_loop(9))



def knapsack_recu(value,weight,size,n):
		
	
	
	if n ==0 or size ==0:
		return 0
	if table[n][size] != -1:
		return table[n][size]	
	elif weight[n-1] <= size:
		table[n][size]=max(value[n-1]+knapsack_recu(value,weight,size-weight[n-1],n-1),knapsack_recu(value,weight,size,n-1))
		#return table[n][size]
	elif weight[n-1]>size:
		table[n][size]=knapsack_recu(value,weight,size,n-1)
		

	return table[n][size]

value =[60,100,120]
weight =[10,20,30]
size =50
n=len(value)	
table =[[-1 for x in range(size+1)]for y in range(n+1)]
print(knapsack_recu(value,weight,size,n))
	
print(table)