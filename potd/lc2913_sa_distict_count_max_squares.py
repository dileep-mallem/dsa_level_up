class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        i,j=0,0
        n=len(nums)
        result=0
        for i in range(n) : 
            for j in range (i,n):
                s=set(nums[i:j+1])
                l=list(s)    
                count=len(l)
                result += count**2 
              
                
        return result    
                
