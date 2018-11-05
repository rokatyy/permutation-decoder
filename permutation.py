from itertools import permutations

def iter_combine(n):
	num_alphabet=''.join([str(i) for i in range(n)])
	return permutations(num_alphabet,n)

def matrix(string,n):
	matr=[]
	m = int(len(string)//n)
	if len(string)%n !=0: m+=1
	for i in range(m):
		matr.append(list(string[i*n:(i+1)*n]))
	return matr
def transformation (matr, index, keyword):
	new_string=''
	for j in range(len(matr)):
		for i in index:
			k = int(i)
			try:
				new_string+=matr[j][k]
			except:
				pass
	if keyword !=None:
		if new_string.find(keyword)>=0: print(new_string)
	else: return(new_string)

def decoding(string,keyword):
	for key in range(7,10):
		variable = iter_combine(key)
		matr = matrix(string,key)
		for i in variable:
			indexes = ''.join(i)
			result = transformation(matr, list(indexes),keyword)
			
def encoding(string, indexes):
	matr = matrix(string, len(indexes))
	return transformation(matr, list(indexes), None)
