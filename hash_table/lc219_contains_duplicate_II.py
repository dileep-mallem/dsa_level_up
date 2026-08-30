class Solution(object):
    def containsNearbyDuplicate(self, nums, k) : 

        d={}
        
        for i,value in enumerate(nums) : 
            if value in d and abs(d[value]-i)<=k:
                    return True 
            d[value]=i # Cahnges to last Index
        return False  