# Hashing , Easy 
# Check Initail befre adding for Reducing Runtime

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Finding Freuency of Each Number 
        d={}
        for i in nums : # O(n)
            if i in d : # Check Keys 
                return True 
            d[i]=1
        return False