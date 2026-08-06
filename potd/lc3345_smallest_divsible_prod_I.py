class Solution(object):
    def smallestNumber(self, n, t):
        while  True : 
            k=n
            prod=1
            while k!=0 : 
                prod*= k % 10  # Product of Digits
                k=k//10 
            if prod%t==0 :
                return n 
            else :
                n += 1 