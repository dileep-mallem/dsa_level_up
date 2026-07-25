# Improve Observations (Developing Cases) , Medium , O(n) , Revisit

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sub Array means It Should be Continupus 
        # 1 . ALl Postive or (Even neg and all pos)-> Procut of all Elemnts 
        # 2 . Odd neg - > Calcuate preeifx and Suffix of that neg , maxx(all prefixes and all Suffix )
        n=len(nums)
        prefix,suffix=1,1
        max_product=nums[0]
        for i in range(n):
            if prefix == 0 :
                prefix=1
            if suffix == 0:
                suffix=1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-1-i]

            max_product=max(max_product,max(prefix,suffix))
        return max_product




        # Brute -> O(n2)

        # s=nums[0]
        # for i in range(0,n-1):
        #     p=nums[i]
        #     for j in range(i+1,n):
        #         p*=nums[j]
        #         if p > s :
        #             s = p 
        # return s if n > 1 else nums[0]