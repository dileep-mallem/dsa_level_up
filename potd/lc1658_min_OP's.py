class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # Edge Cases
        if target < 0:
            return -1  # Sum of all elements is less than x
        if target == 0:
            return len(nums)  # Need to remove all elements
            
        max_len = -1
        curr_sum = 0
        left = 0
        
        # Sliding Window to find the longest subarray that equals target
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            # Shrink the window from the left if the sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
                
            # If we hit the exact target, record the maximum length
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If max_len was updated, return total elements minus the middle subarray length
        return len(nums) - max_len if max_len != -1 else -1
