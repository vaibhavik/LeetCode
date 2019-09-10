import sys
def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a) 

######### LCM ########

def lcm(a,b):
	return a*b / gcd(b%a, a)


a=input()
b=input()
print lcm(a,b)

