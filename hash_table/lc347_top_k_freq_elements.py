# HAshmaps , lambda fn , 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        if n==1 :
            return nums 
        
        d={}
        for i in nums : # O(n)
            d[i]=d.get(i,0)+1
        
        result=sorted(d,key=lambda x : (d[x],x),reverse = True) # (a,b)  based on a , valuef of b into result , reverse = True gets Decneding Order 
        return result[:k]
