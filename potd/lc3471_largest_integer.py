class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int: # type: ignore
        n = len(nums)
        if k == n:
            return max(nums)
        freq={}
        l=0
        r=k-1

        while r < n :
            for i in nums[l:r+1] :
                freq[i]=freq.get(i,0)+1
            l+=1
            r+=1
        m=-1

        for key,value in freq.items():
            if value == 1:
                m=max(m,key)
                result=m 
        return m