class Solution(object):
    def reverseString(self, s):
        l=0
        r=len(s)-1
        while l <=r : # O(logn)
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1

        return s 
s=Solution()
print(s.reverseString(["J","o","n","S","n","o","w"]))