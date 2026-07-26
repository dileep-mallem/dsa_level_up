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
        
        # We can't sort the dictionary 
        # so COnvert HashTable into List(key,value) and it using lamba fn
        l=[] 
        for key , value in d.items(): 
            l.append((key,value))
        s=sorted(l,key= lambda x : (x[1],x[0]),reverse=True)
            
        l2=[]
        for i in s:
            l2.append(i[0])
        return l2[:k]
