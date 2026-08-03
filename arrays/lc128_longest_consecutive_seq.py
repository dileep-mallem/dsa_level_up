# Avg , 
class Solution(object):
  def longestConsecutive(self, nums):
    s = set(nums) # It removes Duplicates
    max_length = 0

    for i in s:
      if i - 1 not in s:
        current_num = i
        current_len = 1

        while current_num + 1 in s:
          current_num += 1
          current_len += 1

        max_length = max(max_length, current_len)

    return max_length
