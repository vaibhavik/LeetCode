def last_digit_fibo_sum(n):
	f=[]
	sum=1
	f.append(0)
	f.append(1)
	for i in range(2,n+1):
		f.append((f[i-1]+f[i-2])%10)
		sum = sum + f[i-1]+f[i-2]%10
	print sum%10


last_digit_fibo_sum(100)
# 5