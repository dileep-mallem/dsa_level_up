class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n=len(nums)

        # fo strictly incresains
        inc=1
        first=nums[0]
        max_length=1
        for i in range(1,n):
            if nums[i]>first : 
                inc+=1
            else : 
                inc=1
            first=nums[i]
            max_length=max(max_length,inc)

        # fo strictly incresains
        dec=1
        first=nums[0]
        max_length2=1
        for i in range(1,n):
            if nums[i]<first : 
                dec+=1
                
            else : 
                dec=1
            first=nums[i]
            max_length2=max(max_length2,dec)

        return max(max_length,max_length2)