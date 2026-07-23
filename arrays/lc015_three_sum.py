# Toics : Arrays , Two Pointer , Diff : MEd 
# Every thing wrote but stuck at edge Cases 
# Revisiit : YES , Fav



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Array should Sorted to restrict Duplicates         
        # Brute Force : Three Loops , in condn , appending 
        # n <=3000 , TC : O(n2) 
        # for o(n2) -> Take one element as no 
        nums.sort()
        result=[] 
        i,n=0,len(nums)
        while i < n-2 :
            # Skip duplicate starting elements
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i + 1
            k = n - 1
            
            while j < k :
                sum = nums[j] + nums[k] + nums[i]
                l2=[nums[i],nums[j],nums[k]]
                if sum == 0 :
                    result.append(l2)
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum > 0 :
                    k-=1 
                else :
                    j+=1 
            i+=1
            
        return result
