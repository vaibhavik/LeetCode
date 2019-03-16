def maxPairProduct(a,numbers):
	m = max(numbers)
	m2 = 0
	for x in numbers:
		if x >= m2 and x <= m:
			m2 = x
	return m*m2 

l = input()
numbers = list(map(int, input().split()))
print (maxPairProduct(l,numbers))

'''
input - len of array 
		space separated numbers in array

output - max product

'''		