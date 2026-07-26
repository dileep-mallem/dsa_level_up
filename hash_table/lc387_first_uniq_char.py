class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s :
            d[i]=d.get(i,0)+1 
        # for key,value in d.items():
        #     if value == 1 :
        #         return s.index(key) It gives O(n**2)
        for i,j in enumerate(s) : # Index : value
            if d[j]==1 :
                return i
        return -1