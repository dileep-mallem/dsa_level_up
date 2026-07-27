# Anagrams , easy 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return True if sorted(s)==sorted(t) else False

        if len(s)!=len(t) :
            return False 
        count=[0]*26 
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1 

        return all(c==0 for c in count)