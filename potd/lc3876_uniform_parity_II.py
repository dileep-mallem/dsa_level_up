class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n=len(nums1)

        evens=[x for x in nums1 if x%2==0]
        odds=[x for x in nums1 if x%2!=0]

        # if nums1 consts all evens or odds , True 
        if len(evens)==n or len(odds)==n : 
            nums2=nums1.copy()
            return True 

        nums2 = []
       
        target_subtrahend = min(odds) # *** not odd[0] otr any other index  #Take any odd number
        
        # If mixed , We make all odd 
        for x in range(n) : 
            if nums1[x]%2!=0 :
                nums2.append(nums1[x])   
            else :  # even 
                if nums1[x] - target_subtrahend >= 1 :
                    nums2.append(nums1[x]-target_subtrahend)
                else :
                    return False
            
        return True 

        # Case 2: Mixed array. We can only make everything odd.
        # This requires the smallest odd number to be less than the smallest even number.
        # if min(odds) < min(evens):
        #     return True
        # return False