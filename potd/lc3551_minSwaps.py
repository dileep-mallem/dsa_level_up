class Solution:
    def minSwaps(self, nums: list[int]) -> int:
       

        def digit_sum(num : int) : 
            total=0
            while num!=0 :
                total += num%10
                num//=10
            return total

        n=len(nums)
        
        # Sort a copy of the array by digit sum. If two sums are equal, sort by value.
        sorted_nums=sorted(nums,key=lambda x : (digit_sum(x),x)) # *
        pos={val:i for i,val in enumerate(sorted_nums)}

        visited=[False]*n
        cycles=0

        for i in range(n) : 
            if not visited[i] : 
                cycles += 1 
                j=i 
                while not visited[j] : 
                    visited[j]=True
                    j=pos[nums[j]]
        return n-cycles