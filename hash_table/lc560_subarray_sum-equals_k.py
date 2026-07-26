# Hashmaps , prefix Sum , medium , O(n) , Revist : YES


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
 
        
        h={0:1} # for if n==1 
        prefix=0
        count=0
        for i in nums :
            prefix+=i
            remove = prefix-k
            if remove in h :
                count +=  h[remove]
            h[prefix]=h.get(prefix,0)+1

        return count