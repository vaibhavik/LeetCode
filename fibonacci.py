def fibo(n):
	f = []
	i = 2
	f.append(0)
	f.append(1)
	while i < n:
		f.append(f[i-2] + f[i-1])
		i = i+1
	print(f)	
	return f[n-1]

print(fibo(10))		 

'''
fibonacci - get nth element
Dynamic
non- recursive
'''