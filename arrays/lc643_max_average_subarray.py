#Sliding Window , Fixed , Medium 

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        old_sum=sum(nums[0:k])
        max_sum=old_sum

        l=0
        r=k-1
        while r < n-1 :
            new_sum = old_sum - nums[l] + nums[r+1] # Decreases TC from O(n*k) to O(n) when we use sum(nums[l:r+1]) Everytime
            if new_sum > max_sum:
                max_sum = new_sum
            old_sum=new_sum 
            l+=1
            r+=1
        
        return max_sum/float(k)
