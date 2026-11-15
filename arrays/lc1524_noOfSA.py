class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Start with even_count = 1 to account for an empty prefix sum of 0
        even_count = 1
        odd_count = 0
        
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                # Current sum is even; pair with previous odd prefix sums
                result += odd_count
                even_count += 1
            else:
                # Current sum is odd; pair with previous even prefix sums
                result += even_count
                odd_count += 1
            print(result)
                
        return result % MOD

s=Solution()

x=s.numOfSubarrays([i for i in range(1,8)]) # 16 