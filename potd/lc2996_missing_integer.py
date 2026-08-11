class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n=len(nums)


        # prefix=[0]*n
        # prefix[0]=nums[0]    # No need we use Sum(for Lowering TC)
        # for i in range(1,n) : 
        #     prefix[i] = prefix[i-1] + nums[i]
            
        # If k=prfix[max_element -1] in nums , k+=1 , return k 
        last_index=n-1 # If All True of COndn , then li=n-1 only
        for i in range(1,n) : 
            if nums[i]!=nums[i-1] + 1 : 
                last_index=i-1
                break
        x=sum(nums[:last_index+1])
        # while x in nums : # Time : O(n) * (no.of.Time)
        #     x+=1
        # return x
        s=set(nums) # O(n)
        while x in s : # O(1) (it(Set) only seacheswhere it Presents not from start everytime)
            x+=1
        return x
