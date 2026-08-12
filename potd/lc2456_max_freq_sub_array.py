# Sliding Window , O(n) , Variable Window 
class Solution :
    def maxSubArray(nums : list,k : int)-> int :
        i=0
        j=0
        max_count=0
        d={}

        for j in range(len(nums)) : 
            d[nums[j]]=d.get(nums[j],0)+1

            while d[nums[j]]>k : # *
                left=nums[i]
                d[left]-=1
                i+=1
            max_count=max(max_count,j-i+1)
        return max_count
