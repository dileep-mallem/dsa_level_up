class Solution(object):
    def threeSumClosest(self, nums, target):

        # Brute : Take Three Loops ( abs(sum - target) , which is min return , TC : Clode to O(n**3) )
        
        # Take l , r and j b/n them and iterate j till r and after moves l ,r till l < r , min comes , O(n logn )

        n=len(nums)
        nums.sort()       
        closest_sum=float('inf')
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue 
            j=i+1
            k=n-1

            while j < k :
                total=nums[i] + nums[j] + nums[k]

                if total==target :
                    return total

                if abs(total-target) < abs(closest_sum-target) :
                    closest_sum = total
                    
                if total > target :
                    k-=1
                else :
                    j+=1
                 
        return closest_sum
s=Solution()
print(s.threeSumClosest([-5,-4,0,0,3,3,4,5],-2))
