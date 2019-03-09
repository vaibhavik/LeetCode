class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {
        "I" :1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        val =0
        i=0
        y = s[::-1]
        #for i in range(0,len(y)):
        while i< len(y):
            if i >= len(y)-1 and mapping.get(y[i-1]) <= mapping.get(y[i]):
                val = val + mapping.get(y[i])
                i=i+1
                #print "add",val

            elif mapping.get(y[i]) <= mapping.get(y[i+1]):
                val = val + mapping.get(y[i])
                i=i+1
                #print "add",val
            else:
                val = val + (mapping.get(y[i]) - mapping.get(y[i+1]))
                i = i+2
                #print "sub",val
        return val