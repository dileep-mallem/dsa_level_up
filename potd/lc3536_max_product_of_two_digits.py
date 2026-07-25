class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in str(n):
            l.append(int(i))
        n1=len(l)
        l.sort()
        return l[n1-1] * l[n1-2] if n1 > 1 else l[0]