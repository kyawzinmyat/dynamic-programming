
def compute_edit_distance_with_memorize(first,second):
	cache=[[None for i in range(len(second))]for j in range(len(first))]
	def recurse(i,j):
		if cache[i-1][j-1]:
			return cache[i-1][j-1]
		if i== 0:
			result = j
		elif j==0:
			result = i
		elif first[i-1]==second[j-1]:
			result = recurse(i-1,j-1)
		else:
			substitute = 1+recurse(i-1,j-1)
			insert = 1 +recurse(i,j-1)
			delete = 1+recurse(i-1,j)
			result=min(substitute,insert,delete)
			cache[i-1][j-1]=result
			print(cache)
		return result
	return recurse(len(first),len(second))
	
def compute_edit_distance_plane(first,second):
	def recurse(i,j):
		if i== 0:
			result = j
		elif j==0:
			result = i
		elif first[i-1]==second[j-1]:
			result = recurse(i-1,j-1)
		else:
			substitute = 1+recurse(i-1,j-1)
			insert = 1 +recurse(i,j-1)
			delete = 1+recurse(i-1,j)
			result=min(substitute,insert,delete)
		return result
	return recurse(len(first),len(second))
	
	
	
	
first ="a cat"
second="the cats"
print(compute_edit_distance_with_memorize(first,second))

