class Solution(object):
    def reverse(self, x):
        x = str(x)
        if(x[0] == '-'):
		    x = x.replace('-','') + '-'
        y = ""
        for i in range(0,len(x)):
		    y = y + x[(len(x)-1)-i]
        if len(y)>1 and y[0] == '0':
		    return int(y[1:len(y)])	
        elif int(y) > 2**31 - 1 or int(y) < -2**31 -1:
		    return 0
        else:
		    return int(y)
