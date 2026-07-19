# Topic : String , can be done by Two Pointer also , Easy , 
# Time : O(n) space : O(n)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=[]
        for char in s.lower() :
            if char.isalnum() :
                result.append(char) # Adding into Empty String is Slower than appending into Lists
        return result[0:] == result[: : -1]