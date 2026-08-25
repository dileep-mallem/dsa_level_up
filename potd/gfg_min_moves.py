class Solution:
    def minMoves(self, arr):
        
        hash={}
        n=len(arr)
        for i in range(n) : 
            hash[arr[i]]=i 
            
        result=1
        m=1
        for i in range(1,n) : 
            if hash[i] < hash[i+1] : 
                result+=1 
                m=max(result,m)
                
            else : 
                result=1
                
                
        return n-m
        
            
        
        
        
