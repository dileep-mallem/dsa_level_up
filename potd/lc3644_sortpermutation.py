class Solution:
    def sortPermutation(self, nums) -> int:
        n=len(nums) 

        if n==1 or nums==sorted(nums) or nums[0]!=0 : 
            return 0 
        
        result=None

        for i in range(1,n) : 
            if nums[i]!=i  : 
                if result==None : 
                    result=nums[i]
                result = result & nums[i]
        return result 