class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        

        # Build Hasp Table 
        hash_table={}
        for i in nums :
            hash_table[i]=hash_table.get(i,0) + 1
        # Check Query : Max Freq Key 
        for key,value in hash_table.items():
            if value > n//2 :
                return key       
    
s=Solution()
x=s.majorityElement([3,3,2,2,3,3])
print(x)