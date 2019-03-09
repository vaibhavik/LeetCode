class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palin =""
        x = str(x)
        for i in range(0,len(x)):
	        palin = palin + x[(len(x)-1)-i]
        if palin == x:
            return True
        else:
            return False
		
        