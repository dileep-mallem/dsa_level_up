class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int: # type: ignore
        j=1
        n=len(nums)
        multiples=(k*i for i in range(1,len(nums)+2))
        s=set(nums)

        for i in multiples : 
            if i not in s : 
                return i 

