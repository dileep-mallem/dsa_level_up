class Solution(object):
    def smallestPalindrome(self, s):
        n=len(s)
        if n==1 :
            return s[0]
        result = ""
        if n%2!=0:
            mid=n//2
        half=n//2
        # We first sort first half add mif (if) and then add reverse first half 
        sorted_1="".join(sorted(s[:half]))
        reverse="".join(reversed(sorted_1))
        if n%2==0:
            result= sorted_1 + reverse 
        else :
            result= sorted_1 + s[mid] +reverse
        return result