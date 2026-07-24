# Topic : Prefix Sum 
# Just replace (Prefix Sum and Suffix SUm) with (Prefix Produt(from i-1 to 0 and pp[0]=1) and Siffix Produt(from i+1 to end , sp[n-1]=1) )
# Tc : O(n) SC : O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        pp=[1]*n
        sp=[1]*n
        
        # Prefix Product 
        for i in range(1,n):
            pp[i]=pp[i-1] * nums[i-1]
        #Suffix Product 
        for i in range(n-2,-1,-1):
            sp[i]=sp[i+1]*nums[i+1]
        # result=[]
        # for i in range(n): 
        #     result.append(pp[i]*sp[i])

        return [ pp[i]*sp[i] for i in range(n) ]