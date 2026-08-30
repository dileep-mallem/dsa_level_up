class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maximum,minimum=max(nums),min(nums)

        n=len(nums)

        if n==1 :
            return 1 

        index_max=nums.index(maximum)
        index_min=nums.index(minimum)

        i,j=min(index_min,index_max),max(index_min,index_max)
        r1=j+1 

        # Delete Both From right 
        r2=n-i 

        # Split 
        r3 = (i+1) + (n-j)

        return min(r1,r2,r3)
