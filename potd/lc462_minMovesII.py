class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # n=len(nums)
        # if n==1 :
        #     return 0 
        # if n==2 :
        #     med=(nums[0]+nums[1])//2
        #     result = abs(med-nums[0]) + abs(med-nums[1])
        #     return result
        # # sum of abs(diff) betwnn nums[i] and median 

        # # finding median 
        # nums.sort()
        
        # mid=n//2 

        # med=(nums[mid-1] + nums[mid]) // 2 if n%2==0 else nums[mid]

        # result=0
        # for i in range(n) : 
        #     result += abs(nums[i]-med)
        # return result

        nums.sort()
        # nums[n // 2] works perfectly as the median for both even and odd lengths
        median = nums[len(nums) // 2]
        
        # Calculate the total moves to bring every element to the median
        return sum(abs(num - median) for num in nums)